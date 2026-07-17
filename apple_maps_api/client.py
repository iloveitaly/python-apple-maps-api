"""Apple Maps Server API client library.

API docs: https://developer.apple.com/documentation/applemapsserverapi

This library provides a Python client for the Apple Maps Server API with JWT-based
authentication, automatic token management, and retry logic.
"""

import logging
import os
import time
from collections.abc import Sequence
from typing import Required, TypedDict, Unpack, overload
from urllib.parse import parse_qs, urlparse

import funcy as f
import httpx2
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
    MapRegion,
    PlaceResults,
    PoiCategory,
    SearchACResultType,
    SearchAutocompleteResponse,
    SearchRegionPriority,
    SearchResponse,
    SearchResultType,
    TokenResponse,
)

log = logging.getLogger(__name__)


def _csv(value: str | Sequence | None) -> str | None:
    """Serialize a string or sequence of values to Apple's comma-separated form."""
    if value is None:
        return None
    if isinstance(value, str):
        return value
    return ",".join(str(v) for v in value)


def _lat_lng_to_apple_str(
    *,
    lat: float | None = None,
    lng: float | None = None,
) -> str | None:
    """Serialize an optional lat/lng pair to Apple's 'lat,lng' string form."""
    if lat is None and lng is None:
        return None

    assert lat is not None and lng is not None, "lat and lng must both be provided"
    return f"{lat},{lng}"


def _search_region(region: MapRegion | None) -> str | None:
    """Serialize MapRegion to Apple's searchRegion form: northLat,eastLng,southLat,westLng."""
    if region is None:
        return None

    return (
        f"{region.northLatitude},{region.eastLongitude},"
        f"{region.southLatitude},{region.westLongitude}"
    )


# shared timeout: 10s connect, 30s read
_TIMEOUT = httpx2.Timeout(connect=10, read=30, write=10, pool=10)

# Auth JWT lifetime is client-chosen; Apple does not document a max for Maps Server API.
# Access tokens from /v1/token are separately ~30 min (Apple-controlled).
# https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api
_DEFAULT_JWT_TTL_SECONDS = 60 * 60


def _is_retryable_http_error(exception: BaseException) -> bool:
    """Return True to retry, False to stop.

    Retries on network-level errors and HTTP 429/5xx.
    All other 4xx errors are permanent failures and should not be retried.
    """
    if not isinstance(exception, httpx2.HTTPError):
        return False

    if isinstance(exception, httpx2.HTTPStatusError):
        status = (
            exception.response.status_code if exception.response is not None else None
        )
        return status == 429 or (status is not None and status >= 500)

    return True


_retry_policy = retry(
    stop=stop_after_attempt(6),
    wait=wait_exponential(multiplier=1, min=0, max=32),
    retry=retry_if_exception(_is_retryable_http_error),
    before_sleep=before_sleep_log(log, logging.INFO),
    reraise=True,
)


class _GeocodeOptionsBase(TypedDict, total=False):
    """Shared optional kwargs for :meth:`AppleMapsClient.geocode`.

    Location params (all optional; different roles):

    - ``lat`` / ``lng``: app-defined point hint; sent as Apple's
      ``searchLocation`` (must pass both). Primary geographic bias.
    - ``search_region``: app-defined bounding-box hint as :class:`MapRegion`.
    - ``user_lat`` / ``user_lng``: the *user's* current position (must pass both).
      Used for ranking/relevance; if ``lat``/``lng`` are omitted, some Apple
      endpoints may fall back to user position as the search hint.
    """

    limit_to_countries: str | Sequence[str]
    lang: str
    search_region: MapRegion
    user_lat: float
    user_lng: float


class GeocodeOptionsLatLng(_GeocodeOptionsBase, total=False):
    """Geocode options with required ``lat`` and ``lng`` location bias."""

    lat: Required[float]
    lng: Required[float]


class GeocodeOptions(_GeocodeOptionsBase, total=False):
    """All optional kwargs for :meth:`AppleMapsClient.geocode`."""

    lat: float
    lng: float


# Location bias is optional; when set both lat and lng are required.
# Overloads below enforce that for pyright; runtime asserts in _lat_lng_to_apple_str.
class _SearchOptionsBase(TypedDict, total=False):
    """Shared optional kwargs for :meth:`AppleMapsClient.search`.

    Location params (all optional; different roles):

    - ``lat`` / ``lng``: app-defined point hint; sent as Apple's
      ``searchLocation`` (must pass both). Primary geographic bias —
      "search near this map point".
    - ``search_region``: app-defined bounding-box hint as :class:`MapRegion`.
    - ``user_lat`` / ``user_lng``: the *user's* current position (must pass both).
      Used for ranking/relevance; Search may fall back to it as
      ``searchLocation`` when ``lat``/``lng`` are omitted.
    """

    categories: str | Sequence[str | PoiCategory]
    exclude_categories: str | Sequence[str | PoiCategory]
    limit_to_countries: str | Sequence[str]
    lang: str
    result_type_filter: str | Sequence[str | SearchResultType]
    search_region: MapRegion
    user_lat: float
    user_lng: float
    search_region_priority: SearchRegionPriority | str
    enable_pagination: bool
    page_token: str
    include_address_categories: str | Sequence[str | AddressCategory]
    exclude_address_categories: str | Sequence[str | AddressCategory]


class SearchOptionsLatLng(_SearchOptionsBase, total=False):
    """Search options with required ``lat`` and ``lng`` location bias."""

    lat: Required[float]
    lng: Required[float]


class SearchOptions(_SearchOptionsBase, total=False):
    """All optional kwargs for :meth:`AppleMapsClient.search`."""

    lat: float
    lng: float


class _AutocompleteOptionsBase(TypedDict, total=False):
    """Shared optional kwargs for :meth:`AppleMapsClient.autocomplete`.

    Location params match search (see :class:`_SearchOptionsBase`):
    ``lat``/``lng`` → ``searchLocation`` bias; ``search_region`` as MapRegion;
    ``user_lat``/``user_lng`` is the user's position (ranking; may fall back as
    ``searchLocation`` when lat/lng are omitted).
    """

    limit_to_countries: str | Sequence[str]
    lang: str
    result_type_filter: str | Sequence[str | SearchACResultType]
    include_poi_categories: str | Sequence[str | PoiCategory]
    exclude_poi_categories: str | Sequence[str | PoiCategory]
    search_region: MapRegion
    user_lat: float
    user_lng: float
    search_region_priority: SearchRegionPriority | str
    include_address_categories: str | Sequence[str | AddressCategory]
    exclude_address_categories: str | Sequence[str | AddressCategory]


class AutocompleteOptionsLatLng(_AutocompleteOptionsBase, total=False):
    """Autocomplete options with required ``lat`` and ``lng`` location bias."""

    lat: Required[float]
    lng: Required[float]


class AutocompleteOptions(_AutocompleteOptionsBase, total=False):
    """All optional kwargs for :meth:`AppleMapsClient.autocomplete`."""

    lat: float
    lng: float


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

    def _create_jwt(self, *, ttl_seconds: int = _DEFAULT_JWT_TTL_SECONDS) -> str:
        """Build an ES256-signed JWT for MapKit JS or /v1/token exchange.

        Header: alg=ES256, kid, typ=JWT. Payload: iss, iat, exp, optional origin.

        Spec:
        https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api

        Vendored mirror (offline):
        docs/apple_maps_documentation/developer.apple.com_documentation_applemapsserverapi_creating-and-using-tokens-with-maps-server-api.md

        This is the *auth JWT* — a credential proving we own the Maps private key.
        For Server API use it is exchanged for an *access token* (see _fetch_token).
        For MapKit JS it is returned directly via create_mapkit_token().
        """
        assert ttl_seconds > 0, "ttl_seconds must be positive"

        now = int(time.time())
        payload: dict[str, object] = {
            "iss": self.team_id,
            "iat": now,
            "exp": now + ttl_seconds,
        }

        if self.origin:
            payload["origin"] = self.origin

        # ES256 + kid required by Apple Maps token spec (link in docstring above)
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

        Spec: https://developer.apple.com/documentation/applemapsserverapi/-v1-token
        """
        response = httpx2.get(
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
          2. _fetch_token()  → GETs /v1/token, gets back an access token
          3. access token    → cached in-process; reused until 60 s before expiry

        The access token is what gets sent as `Authorization: Bearer` on every
        Maps API call. The auth JWT is a one-shot credential and is discarded.

        Spec:
        https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api
        https://developer.apple.com/documentation/applemapsserverapi/-v1-token
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

        Spec: https://developer.apple.com/documentation/applemapsserverapi/-v1-token
        """
        return self._ensure_token()

    def create_mapkit_token(
        self, *, ttl_seconds: int = _DEFAULT_JWT_TTL_SECONDS
    ) -> str:
        """Return a signed JWT for MapKit JS browser initialization.

        MapKit JS requires the raw signed JWT, not the Server API access token.
        Pass this to the `authorizationCallback` done() function.
        If `origin` was set on the client, the token is restricted to that domain.

        :param ttl_seconds: JWT lifetime in seconds (default: 1 hour).
            Apple does not document a maximum for Maps tokens.

        Spec:
        https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api
        https://developer.apple.com/documentation/mapkitjs/creating-and-using-tokens-with-mapkit-js
        """
        return self._create_jwt(ttl_seconds=ttl_seconds)

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

        response = httpx2.get(url, params=params, headers=headers, timeout=_TIMEOUT)
        response.raise_for_status()

        return response.json()

    @overload
    def geocode(
        self, query: str, **kwargs: Unpack[GeocodeOptionsLatLng]
    ) -> PlaceResults: ...

    @overload
    def geocode(
        self, query: str, **kwargs: Unpack[_GeocodeOptionsBase]
    ) -> PlaceResults: ...

    def geocode(self, query: str, **kwargs: Unpack[GeocodeOptions]) -> PlaceResults:
        """Convert an address string to coordinates.

        Maps to GET /v1/geocode.

        :param query: Address to geocode (e.g., "1 Apple Park Way").
        :param limit_to_countries: ISO 3166-1 alpha-2 country codes to limit results
            (e.g. ``["US", "CA"]``).
        :param lang: BCP 47 language code (default: "en-US").
        :param lat: Latitude for app-defined search bias (must pass with lng).
            Sent as Apple's ``searchLocation``.
        :param lng: Longitude for app-defined search bias (must pass with lat).
        :param search_region: App-defined bounding-box hint as :class:`MapRegion`.
        :param user_lat: Latitude of the user's position (must pass with user_lng).
            Used for ranking/relevance; if ``lat``/``lng`` are omitted, some
            endpoints may fall back to this as the search hint.
        :param user_lng: Longitude of the user's position (must pass with user_lat).
        """
        if not query:
            raise ValueError("query must be provided.")

        params: dict[str, str] = dict(
            f.compact(
                {
                    "q": query,
                    "limitToCountries": _csv(kwargs.get("limit_to_countries")),
                    "lang": kwargs.get("lang"),
                    "searchLocation": _lat_lng_to_apple_str(
                        lat=kwargs.get("lat"),
                        lng=kwargs.get("lng"),
                    ),
                    "searchRegion": _search_region(kwargs.get("search_region")),
                    "userLocation": _lat_lng_to_apple_str(
                        lat=kwargs.get("user_lat"),
                        lng=kwargs.get("user_lng"),
                    ),
                }
            )
        )

        raw = self._make_request("/v1/geocode", params)
        return PlaceResults.model_validate(raw)

    def reverse_geocode(
        self,
        *,
        lat: float,
        lng: float,
        lang: str | None = None,
    ) -> PlaceResults:
        """Convert coordinates to an address.

        Maps to GET /v1/reverseGeocode.

        :param lat: Latitude of the point to reverse geocode.
        :param lng: Longitude of the point to reverse geocode.
        :param lang: BCP 47 language code (default: "en-US").
        """
        params: dict[str, str] = dict(f.compact({"loc": f"{lat},{lng}", "lang": lang}))

        raw = self._make_request("/v1/reverseGeocode", params)
        return PlaceResults.model_validate(raw)

    @overload
    def search(
        self, query: str, **kwargs: Unpack[SearchOptionsLatLng]
    ) -> SearchResponse: ...

    @overload
    def search(
        self, query: str, **kwargs: Unpack[_SearchOptionsBase]
    ) -> SearchResponse: ...

    def search(self, query: str, **kwargs: Unpack[SearchOptions]) -> SearchResponse:
        """Search for places by name or category.

        Maps to GET /v1/search.

        Location bias (optional): pass ``lat=`` and ``lng=`` together.

        :param query: Search query (e.g., "coffee", "Apple Park").
        :param lat: Latitude for app-defined search bias (must pass with lng).
            Sent as Apple's ``searchLocation`` — "search near this map point".
        :param lng: Longitude for app-defined search bias (must pass with lat).
        :param categories: POI categories to include (e.g. ``["MovieTheater", "Cafe"]``).
        :param exclude_categories: POI categories to exclude (e.g. ``["Parking"]``).
        :param limit_to_countries: ISO 3166-1 alpha-2 country codes
            (e.g. ``["US", "CA"]``).
        :param lang: BCP 47 language code (default: "en-US").
        :param result_type_filter: Result types (e.g. ``["Poi", "Address"]``).
        :param search_region: App-defined bounding-box hint as :class:`MapRegion`.
        :param user_lat: Latitude of the user's position (must pass with user_lng).
            Used for ranking/relevance; Search may fall back to it as
            ``searchLocation`` when ``lat``/``lng`` are omitted.
        :param user_lng: Longitude of the user's position (must pass with user_lat).
        :param search_region_priority: Importance of ``search_region``
            (:class:`SearchRegionPriority` or ``"default"`` / ``"required"``).
        :param enable_pagination: Request paginated results.
        :param page_token: Token identifying which page of results to return.
        :param include_address_categories: Address categories to include
            (e.g. ``["AdministrativeArea"]``).
        :param exclude_address_categories: Address categories to exclude.
        """
        if not query:
            raise ValueError("query must be provided.")

        raw_params: dict[str, object] = {
            "q": query,
            "searchLocation": _lat_lng_to_apple_str(
                lat=kwargs.get("lat"),
                lng=kwargs.get("lng"),
            ),
            "includePoiCategories": _csv(kwargs.get("categories")),
            "excludePoiCategories": _csv(kwargs.get("exclude_categories")),
            "limitToCountries": _csv(kwargs.get("limit_to_countries")),
            "lang": kwargs.get("lang"),
            "resultTypeFilter": _csv(kwargs.get("result_type_filter")),
            "searchRegion": _search_region(kwargs.get("search_region")),
            "userLocation": _lat_lng_to_apple_str(
                lat=kwargs.get("user_lat"),
                lng=kwargs.get("user_lng"),
            ),
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

    @overload
    def autocomplete(
        self, query: str, **kwargs: Unpack[AutocompleteOptionsLatLng]
    ) -> SearchAutocompleteResponse: ...

    @overload
    def autocomplete(
        self, query: str, **kwargs: Unpack[_AutocompleteOptionsBase]
    ) -> SearchAutocompleteResponse: ...

    def autocomplete(
        self, query: str, **kwargs: Unpack[AutocompleteOptions]
    ) -> SearchAutocompleteResponse:
        """Autocomplete partial addresses and place names.

        Maps to GET /v1/searchAutocomplete.

        Location bias (optional): pass ``lat=`` and ``lng=`` together.

        Result count is fixed by Apple; the API has no limit/maxResults parameter.
        For more results, use search() (supports enable_pagination) or
        search_completion() to expand a single autocomplete hit.

        :param query: Partial address or place name to autocomplete.
        :param lat: Latitude for app-defined search bias (must pass with lng).
            Sent as Apple's ``searchLocation`` — "search near this map point".
        :param lng: Longitude for app-defined search bias (must pass with lat).
        :param limit_to_countries: ISO 3166-1 alpha-2 country codes
            (e.g. ``["US", "CA"]``).
        :param lang: BCP 47 language code (default: "en-US").
        :param result_type_filter: Result types (e.g. ``["Address", "Poi"]``).
        :param include_poi_categories: POI categories to include
            (e.g. ``["Cafe"]``).
        :param exclude_poi_categories: POI categories to exclude.
        :param search_region: App-defined bounding-box hint as :class:`MapRegion`.
        :param user_lat: Latitude of the user's position (must pass with user_lng).
            Used for ranking/relevance; may fall back as ``searchLocation``
            when ``lat``/``lng`` are omitted.
        :param user_lng: Longitude of the user's position (must pass with user_lat).
        :param search_region_priority: Importance of ``search_region``
            (:class:`SearchRegionPriority` or ``"default"`` / ``"required"``).
        :param include_address_categories: Address categories to include.
        :param exclude_address_categories: Address categories to exclude.
        """
        if not query:
            raise ValueError("query must be provided.")

        params: dict[str, str] = dict(
            f.compact(
                {
                    "q": query,
                    "searchLocation": _lat_lng_to_apple_str(
                        lat=kwargs.get("lat"),
                        lng=kwargs.get("lng"),
                    ),
                    # Note: Apple maps documentation says to use 'limitToCountries' param but it seems to work only with almost full address
                    "limitToCountries": _csv(kwargs.get("limit_to_countries")),
                    "lang": kwargs.get("lang"),
                    "resultTypeFilter": _csv(kwargs.get("result_type_filter")),
                    "includePoiCategories": _csv(kwargs.get("include_poi_categories")),
                    "excludePoiCategories": _csv(kwargs.get("exclude_poi_categories")),
                    "searchRegion": _search_region(kwargs.get("search_region")),
                    "userLocation": _lat_lng_to_apple_str(
                        lat=kwargs.get("user_lat"),
                        lng=kwargs.get("user_lng"),
                    ),
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
