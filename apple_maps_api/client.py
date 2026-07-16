"""Apple Maps Server API client library.

API docs: https://developer.apple.com/documentation/applemapsserverapi

This library provides a Python client for the Apple Maps Server API with JWT-based
authentication, automatic token management, and retry logic.
"""

import logging
import os
import time
from collections.abc import Sequence
from typing import TypedDict, Unpack
from urllib.parse import parse_qs, urlparse

import funcy as f
import httpx
import jwt
from tenacity import (
    before_sleep_log,
    retry,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from apple_maps_api.models import (
    AddressCategory,
    AutocompleteResult,
    Location,
    PlaceResults,
    PoiCategory,
    SearchACResultType,
    SearchAutocompleteResponse,
    SearchResponse,
    SearchResultType,
    TokenResponse,
)

log = logging.getLogger(__name__)


def _csv(value: str | Sequence | None) -> str | None:
    """Serialize a plain string or a sequence of StrEnum values to a comma-separated string."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return ",".join(str(v) for v in value)


# shared timeout: 10s connect, 30s read
_TIMEOUT = httpx.Timeout(connect=10, read=30, write=10, pool=10)


def _is_retryable_httpx_error(exception: BaseException) -> bool:
    """Return True to retry, False to stop.

    Retries on network-level errors and HTTP 429/5xx.
    All other 4xx errors are permanent failures and should not be retried.
    """
    if not isinstance(exception, httpx.HTTPError):
        return False

    if isinstance(exception, httpx.HTTPStatusError):
        status = (
            exception.response.status_code if exception.response is not None else None
        )
        return status == 429 or (status is not None and status >= 500)

    return True


_retry_policy = retry(
    stop=stop_after_attempt(6),
    wait=wait_exponential(multiplier=1, min=0, max=32),
    retry=retry_if_exception(_is_retryable_httpx_error),
    before_sleep=before_sleep_log(log, logging.INFO),
    reraise=True,
)


class GeocodeOptions(TypedDict, total=False):
    limit_to_countries: str
    lang: str
    search_location: str
    search_region: str
    user_location: str


class ReverseGeocodeOptions(TypedDict, total=False):
    lang: str


class SearchOptions(TypedDict, total=False):
    near: str
    categories: str | Sequence[PoiCategory]
    exclude_categories: str | Sequence[PoiCategory]
    limit_to_countries: str
    lang: str
    result_type_filter: str | Sequence[SearchResultType]
    search_region: str
    user_location: str
    search_region_priority: str
    enable_pagination: bool
    page_token: str
    include_address_categories: str | Sequence[AddressCategory]
    exclude_address_categories: str | Sequence[AddressCategory]


class AutocompleteOptions(TypedDict, total=False):
    near: str | None
    limit_to_countries: str | None
    lang: str | None
    result_type_filter: str | Sequence[SearchACResultType] | None
    include_poi_categories: str | Sequence[PoiCategory] | None
    exclude_poi_categories: str | Sequence[PoiCategory] | None
    search_region: str | None
    user_location: str | None
    search_region_priority: str | None
    include_address_categories: str | Sequence[AddressCategory] | None
    exclude_address_categories: str | Sequence[AddressCategory] | None


class AppleMapsClient:
    """A client for the Apple Maps Server API.

    Handles JWT-based authentication with automatic token refresh,
    and provides methods for geocoding, reverse geocoding, search, and autocomplete.
    """

    def __init__(
        self, *, team_id: str, key_id: str, private_key: str, origin: str | None = None
    ):
        """Initialize the client.

        :param team_id: Apple Developer Team ID (10-character string).
        :param key_id: Maps key identifier from Apple Developer account.
        :param private_key: ES256 private key, either PEM-encoded or raw base64 DER.
        :param origin: Optional domain restriction for MapKit JS tokens (e.g., "https://example.com").
        """
        if not team_id:
            raise ValueError("team_id must be provided.")

        if not key_id:
            raise ValueError("key_id must be provided.")

        if not private_key:
            raise ValueError("private_key must be provided.")

        self.team_id = team_id
        self.key_id = key_id
        self.origin = origin

        # accept both PEM-formatted keys and raw base64 DER (no PEM wrapping)
        stripped = private_key.strip()
        if not stripped.startswith("-----BEGIN"):
            stripped = (
                f"-----BEGIN PRIVATE KEY-----\n{stripped}\n-----END PRIVATE KEY-----"
            )

        self.private_key = stripped
        self.base_url = "https://maps-api.apple.com"

        self._access_token: str | None = None
        self._token_expires_at: float = 0.0

    @classmethod
    def from_env(cls) -> "AppleMapsClient":
        """Construct a client from APPLE_MAPS_* environment variables.

        Required:
        - APPLE_MAPS_TEAM_ID
        - APPLE_MAPS_KEY_ID
        - APPLE_MAPS_P8_KEY

        Optional:
        - APPLE_MAPS_ORIGIN
        """
        team_id = os.environ.get("APPLE_MAPS_TEAM_ID", "")
        key_id = os.environ.get("APPLE_MAPS_KEY_ID", "")
        private_key = os.environ.get("APPLE_MAPS_P8_KEY", "")
        origin = os.environ.get("APPLE_MAPS_ORIGIN") or None

        missing = [
            name
            for name, value in (
                ("APPLE_MAPS_TEAM_ID", team_id),
                ("APPLE_MAPS_KEY_ID", key_id),
                ("APPLE_MAPS_P8_KEY", private_key),
            )
            if not value
        ]
        if missing:
            raise ValueError(
                f"missing required environment variables: {', '.join(missing)}"
            )

        return cls(
            team_id=team_id,
            key_id=key_id,
            private_key=private_key,
            origin=origin,
        )

    def _create_jwt(self) -> str:
        """Build a short-lived ES256-signed JWT used only to call /v1/token.

        This is the *auth JWT* — a credential proving we own the Maps private key.
        Apple validates it and exchanges it for an *access token* (see _fetch_token).
        It is never sent to the Maps API directly; it is never exposed to clients.
        """
        now = int(time.time())
        payload: dict[str, object] = {
            "iss": self.team_id,
            "iat": now,
            "exp": now + 30 * 60,
        }

        if self.origin:
            payload["origin"] = self.origin

        return jwt.encode(
            payload,
            self.private_key,
            algorithm="ES256",
            headers={"kid": self.key_id},
        )

    @_retry_policy
    def _fetch_token(self, auth_jwt: str) -> TokenResponse:
        """Exchange the auth JWT for a short-lived Maps access token.

        Calls GET /v1/token with the auth JWT in the Authorization header.
        Apple returns an *access token* (Bearer) valid for ~30 minutes that
        authorises all subsequent Maps API requests (geocode, search, etc.).
        """
        response = httpx.get(
            f"{self.base_url}/v1/token",
            headers={"Authorization": f"Bearer {auth_jwt}"},
            timeout=_TIMEOUT,
        )
        response.raise_for_status()

        return TokenResponse.model_validate(response.json())

    def _ensure_token(self) -> str:
        """Return a valid access token, fetching a new one if needed.

        Auth flow:
          1. _create_jwt()   → signs a fresh auth JWT with our ES256 private key
          2. _fetch_token()  → POSTs it to /v1/token, gets back an access token
          3. access token    → cached in-process; reused until 60 s before expiry

        The access token is what gets sent as `Authorization: Bearer` on every
        Maps API call. The auth JWT is a one-shot credential and is discarded.
        """
        if self._access_token and time.time() < self._token_expires_at - 60:
            return self._access_token

        auth_jwt = self._create_jwt()
        token_response = self._fetch_token(auth_jwt)
        self._access_token = token_response.accessToken
        self._token_expires_at = time.time() + token_response.expiresInSeconds

        return self._access_token

    def create_token(self) -> str:
        """Return a valid Maps access token for Apple Maps Server API use.

        This is the *access token* (not the auth JWT) suitable for server-side
        API calls (geocode, search, etc.). It is NOT suitable for MapKit JS.
        Use `create_mapkit_token()` for browser-side MapKit JS initialization.
        """
        return self._ensure_token()

    def create_mapkit_token(self) -> str:
        """Return a signed JWT for MapKit JS browser initialization.

        MapKit JS requires the raw signed JWT, not the Server API access token.
        Pass this to the `authorizationCallback` done() function.
        If `origin` was set on the client, the token is restricted to that domain.
        """
        return self._create_jwt()

    @_retry_policy
    def _make_request(self, path: str, params: dict[str, str]) -> dict[str, object]:
        """Make an authenticated GET request to the Apple Maps API.

        :param path: API endpoint path (e.g., '/v1/geocode').
        :param params: Query parameters.
        :return: JSON response as a dictionary.
        """
        token = self._ensure_token()
        url = f"{self.base_url}{path}"
        headers = {"Authorization": f"Bearer {token}"}

        response = httpx.get(url, params=params, headers=headers, timeout=_TIMEOUT)
        response.raise_for_status()

        return response.json()

    def geocode(self, query: str, **kwargs: Unpack[GeocodeOptions]) -> PlaceResults:
        """Convert an address string to coordinates.

        Maps to GET /v1/geocode.

        :param query: Address to geocode (e.g., "1 Apple Park Way").
        :param limit_to_countries: Comma-separated ISO 3166-1 alpha-2 country codes to limit results.
        :param lang: BCP 47 language code (default: "en-US").
        :param search_location: Lat/lng hint for search bias (e.g., "37.78,-122.42").
        :param search_region: Bounding box hint as "northLat,eastLng,southLat,westLng".
        :param user_location: User's current location as "lat,lng".
        """
        if not query:
            raise ValueError("query must be provided.")

        params: dict[str, str] = dict(
            f.compact(
                {
                    "q": query,
                    "limitToCountries": kwargs.get("limit_to_countries"),
                    "lang": kwargs.get("lang"),
                    "searchLocation": kwargs.get("search_location"),
                    "searchRegion": kwargs.get("search_region"),
                    "userLocation": kwargs.get("user_location"),
                }
            )
        )

        raw = self._make_request("/v1/geocode", params)
        return PlaceResults.model_validate(raw)

    def reverse_geocode(
        self,
        coordinates: tuple[float, float] | Location,
        **kwargs: Unpack[ReverseGeocodeOptions],
    ) -> PlaceResults:
        """Convert coordinates to an address.

        Maps to GET /v1/reverseGeocode.

        :param coordinates: (latitude, longitude) tuple or Location object.
        :param lang: BCP 47 language code (default: "en-US").
        """
        if isinstance(coordinates, Location):
            loc_str = f"{coordinates.latitude},{coordinates.longitude}"
        else:
            loc_str = f"{coordinates[0]},{coordinates[1]}"

        params: dict[str, str] = dict(
            f.compact({"loc": loc_str, "lang": kwargs.get("lang")})
        )

        raw = self._make_request("/v1/reverseGeocode", params)
        return PlaceResults.model_validate(raw)

    def search(self, query: str, **kwargs: Unpack[SearchOptions]) -> SearchResponse:
        """Search for places by name or category.

        Maps to GET /v1/search.

        :param query: Search query (e.g., "coffee", "Apple Park").
        :param near: Location bias as "lat,lng" (maps to searchLocation).
        :param categories: Comma-separated POI categories to include (e.g., "MovieTheater").
        :param exclude_categories: Comma-separated POI categories to exclude.
        :param limit_to_countries: Comma-separated ISO 3166-1 alpha-2 country codes to limit results.
        :param lang: BCP 47 language code (default: "en-US").
        :param result_type_filter: Comma-separated result types (e.g., "Poi", "Address").
        :param search_region: Bounding box hint as "northLat,eastLng,southLat,westLng".
        :param user_location: User's current location as "lat,lng".
        :param search_region_priority: "default" or "required".
        :param enable_pagination: Request paginated results.
        :param page_token: Token identifying which page of results to return.
        :param include_address_categories: Comma-separated AddressCategory values to include.
        :param exclude_address_categories: Comma-separated AddressCategory values to exclude.
        """
        if not query:
            raise ValueError("query must be provided.")

        raw_params: dict[str, object] = {
            "q": query,
            "searchLocation": kwargs.get("near"),
            "includePoiCategories": _csv(kwargs.get("categories")),
            "excludePoiCategories": _csv(kwargs.get("exclude_categories")),
            "limitToCountries": kwargs.get("limit_to_countries"),
            "lang": kwargs.get("lang"),
            "resultTypeFilter": _csv(kwargs.get("result_type_filter")),
            "searchRegion": kwargs.get("search_region"),
            "userLocation": kwargs.get("user_location"),
            "searchRegionPriority": kwargs.get("search_region_priority"),
            "pageToken": kwargs.get("page_token"),
            "includeAddressCategories": _csv(kwargs.get("include_address_categories")),
            "excludeAddressCategories": _csv(kwargs.get("exclude_address_categories")),
        }
        if kwargs.get("enable_pagination"):
            raw_params["enablePagination"] = "true"

        params: dict[str, str] = dict(f.compact(raw_params))

        raw = self._make_request("/v1/search", params)
        return SearchResponse.model_validate(raw)

    def autocomplete(
        self, query: str, **kwargs: Unpack[AutocompleteOptions]
    ) -> SearchAutocompleteResponse:
        """Autocomplete partial addresses and place names.

        Maps to GET /v1/searchAutocomplete.

        :param query: Partial address or place name to autocomplete.
        :param near: Location bias as "lat,lng" to prefer nearby results.
        :param limit_to_countries: Comma-separated ISO 3166-1 alpha-2 country codes to limit results.
        :param lang: BCP 47 language code (default: "en-US").
        :param result_type_filter: Comma-separated result types (e.g., "Address", "Poi").
        :param include_poi_categories: Comma-separated POI categories to include.
        :param exclude_poi_categories: Comma-separated POI categories to exclude.
        :param search_region: Bounding box hint as "northLat,eastLng,southLat,westLng".
        :param user_location: User's current location as "lat,lng".
        :param search_region_priority: "default" or "required".
        :param include_address_categories: Comma-separated AddressCategory values to include.
        :param exclude_address_categories: Comma-separated AddressCategory values to exclude.
        """
        if not query:
            raise ValueError("query must be provided.")

        params: dict[str, str] = dict(
            f.compact(
                {
                    "q": query,
                    "searchLocation": kwargs.get("near"),
                    # Note: Apple maps documentation says to use 'limitToCountries' param but it seems to work only with almost full address
                    "limitToCountries": kwargs.get("limit_to_countries"),
                    "lang": kwargs.get("lang"),
                    "resultTypeFilter": _csv(kwargs.get("result_type_filter")),
                    "includePoiCategories": _csv(kwargs.get("include_poi_categories")),
                    "excludePoiCategories": _csv(kwargs.get("exclude_poi_categories")),
                    "searchRegion": kwargs.get("search_region"),
                    "userLocation": kwargs.get("user_location"),
                    "searchRegionPriority": kwargs.get("search_region_priority"),
                    "includeAddressCategories": _csv(
                        kwargs.get("include_address_categories")
                    ),
                    "excludeAddressCategories": _csv(
                        kwargs.get("exclude_address_categories")
                    ),
                }
            )
        )

        raw = self._make_request("/v1/searchAutocomplete", params)
        return SearchAutocompleteResponse.model_validate(raw)

    def search_completion(
        self,
        completion: AutocompleteResult | str,
        *,
        lang: str | None = None,
    ) -> SearchResponse:
        """Resolve an autocomplete suggestion to full search results.

        Maps to GET /v1/search using the completionUrl from an AutocompleteResult.
        The completionUrl already encodes the query and opaque metadata Apple needs
        to return precise results for the suggestion.

        :param completion: An AutocompleteResult or its completionUrl string.
        :param lang: BCP 47 language code (e.g., "en-US"). Apple does not carry the
            language through the completionUrl, so callers must re-specify it here.
        :raises ValueError: If the completion has no completionUrl.
        """
        if isinstance(completion, AutocompleteResult):
            url_str = completion.completionUrl
            if not url_str:
                raise ValueError("AutocompleteResult has no completionUrl.")
        else:
            url_str = completion

        parsed = urlparse(url_str)
        params: dict[str, str] = {
            k: v[0] for k, v in parse_qs(parsed.query, keep_blank_values=True).items()
        }
        if lang is not None:
            params["lang"] = lang

        raw = self._make_request(parsed.path, params)
        return SearchResponse.model_validate(raw)
