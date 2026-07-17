"""Tests for AppleMapsClient."""

import httpx2
import pytest
import respx

from apple_maps_api import AppleMapsClient, SearchRegionPriority
from apple_maps_api.client import _lat_lng_to_apple_str
from apple_maps_api.models import (
    MapRegion,
    PlaceResults,
    SearchAutocompleteResponse,
    SearchResponse,
)

from tests.constants import (
    SAMPLE_AUTOCOMPLETE_RESPONSE,
    SAMPLE_GEOCODE_RESPONSE,
    SAMPLE_SEARCH_RESPONSE,
    TEST_PRIVATE_KEY,
    TOKEN_RESPONSE,
)


@pytest.fixture
def apple_client(monkeypatch: pytest.MonkeyPatch) -> AppleMapsClient:
    client = AppleMapsClient(
        team_id="TEAM123456",
        key_id="KEY1234567",
        private_key=TEST_PRIVATE_KEY,
    )
    monkeypatch.setattr(client, "_create_jwt", lambda **kwargs: "test_jwt")
    return client


def mock_token(httpx2_mock: respx.Router) -> respx.Route:
    """Set up mock for /v1/token endpoint."""
    return httpx2_mock.get("https://maps-api.apple.com/v1/token").respond(
        json=TOKEN_RESPONSE
    )


class TestAppleMapsClientInit:
    def test_init_valid(self):
        client = AppleMapsClient(
            team_id="TEAM123456",
            key_id="KEY1234567",
            private_key=TEST_PRIVATE_KEY,
        )

        assert client.team_id == "TEAM123456"
        assert client.base_url == "https://maps-api.apple.com"

    def test_init_empty_team_id(self):
        with pytest.raises(ValueError, match="team_id must be provided"):
            AppleMapsClient(team_id="", key_id="KEY", private_key=TEST_PRIVATE_KEY)

    def test_init_empty_key_id(self):
        with pytest.raises(ValueError, match="key_id must be provided"):
            AppleMapsClient(team_id="TEAM", key_id="", private_key=TEST_PRIVATE_KEY)

    def test_init_empty_private_key(self):
        with pytest.raises(ValueError, match="private_key must be provided"):
            AppleMapsClient(team_id="TEAM", key_id="KEY", private_key="")

    def test_from_env_success(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("APPLE_MAPS_TEAM_ID", "TEAM123456")
        monkeypatch.setenv("APPLE_MAPS_KEY_ID", "KEY1234567")
        monkeypatch.setenv("APPLE_MAPS_P8_KEY", TEST_PRIVATE_KEY)

        client = AppleMapsClient.from_env()

        assert client.team_id == "TEAM123456"
        assert client.key_id == "KEY1234567"
        assert client.origin is None

    def test_from_env_with_origin(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("APPLE_MAPS_TEAM_ID", "TEAM123456")
        monkeypatch.setenv("APPLE_MAPS_KEY_ID", "KEY1234567")
        monkeypatch.setenv("APPLE_MAPS_P8_KEY", TEST_PRIVATE_KEY)
        monkeypatch.setenv("APPLE_MAPS_ORIGIN", "https://example.com")

        client = AppleMapsClient.from_env()

        assert client.origin == "https://example.com"

    def test_from_env_one_missing(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.setenv("APPLE_MAPS_TEAM_ID", "TEAM123456")
        monkeypatch.setenv("APPLE_MAPS_KEY_ID", "KEY1234567")
        monkeypatch.delenv("APPLE_MAPS_P8_KEY", raising=False)

        with pytest.raises(ValueError, match="APPLE_MAPS_P8_KEY"):
            AppleMapsClient.from_env()

    def test_from_env_all_missing(self, monkeypatch: pytest.MonkeyPatch):
        monkeypatch.delenv("APPLE_MAPS_TEAM_ID", raising=False)
        monkeypatch.delenv("APPLE_MAPS_KEY_ID", raising=False)
        monkeypatch.delenv("APPLE_MAPS_P8_KEY", raising=False)

        with pytest.raises(
            ValueError,
            match="APPLE_MAPS_TEAM_ID.*APPLE_MAPS_KEY_ID.*APPLE_MAPS_P8_KEY",
        ):
            AppleMapsClient.from_env()

    def test_from_env_empty_string_counts_as_missing(
        self, monkeypatch: pytest.MonkeyPatch
    ):
        monkeypatch.setenv("APPLE_MAPS_TEAM_ID", "")
        monkeypatch.setenv("APPLE_MAPS_KEY_ID", "KEY1234567")
        monkeypatch.setenv("APPLE_MAPS_P8_KEY", TEST_PRIVATE_KEY)

        with pytest.raises(ValueError, match="APPLE_MAPS_TEAM_ID"):
            AppleMapsClient.from_env()


class TestGeocode:
    def test_geocode_success(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        result = apple_client.geocode("1 Apple Park Way, Cupertino, CA")

        assert isinstance(result, PlaceResults)
        assert len(result.results) == 1
        assert result.results[0].structuredAddress is not None
        assert result.results[0].structuredAddress.locality == "Cupertino"

    def test_geocode_with_params(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        apple_client.geocode("Apple Park", limit_to_countries="US", lang="en-US")

        assert route.called
        request = route.calls.last.request
        assert "q=Apple+Park" in str(request.url)
        assert "limitToCountries=US" in str(request.url)
        assert "lang=en-US" in str(request.url)

    def test_geocode_empty_query(self, apple_client: AppleMapsClient):
        with pytest.raises(ValueError, match="query must be provided"):
            apple_client.geocode("")


class TestReverseGeocode:
    def test_reverse_geocode_success(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/reverseGeocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        result = apple_client.reverse_geocode(lat=37.3349, lng=-122.0090)

        assert isinstance(result, PlaceResults)
        assert len(result.results) == 1

    def test_reverse_geocode_sends_loc_param(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/reverseGeocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        apple_client.reverse_geocode(lat=37.3349, lng=-122.0090)

        assert route.called
        request = route.calls.last.request
        assert "loc=37.3349" in str(request.url)
        assert "-122.009" in str(request.url)


class TestSearch:
    def test_search_success(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        result = apple_client.search(query="Apple Park")

        assert isinstance(result, SearchResponse)
        assert len(result.results) == 1
        assert result.results[0].poiCategory == "Landmark"
        assert result.displayMapRegion is not None

    def test_search_with_params(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        apple_client.search(
            query="coffee",
            lat=37.334,
            lng=-122.009,
            categories="Cafe",
            limit_to_countries="US",
        )

        assert route.called
        request = route.calls.last.request
        assert "q=coffee" in str(request.url)
        assert "searchLocation=37.334" in str(request.url)
        assert "includePoiCategories=Cafe" in str(request.url)
        assert "limitToCountries=US" in str(request.url)

    def test_search_with_lat_lng(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        apple_client.search(query="coffee", lat=37.334, lng=-122.009)

        assert route.called
        request = route.calls.last.request
        assert "searchLocation=37.334" in str(request.url)
        assert "-122.009" in str(request.url)

    def test_search_with_user_lat_lng(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        apple_client.search(query="coffee", user_lat=37.334, user_lng=-122.009)

        assert route.called
        request = route.calls.last.request
        assert "userLocation=37.334" in str(request.url)
        assert "-122.009" in str(request.url)

    def test_search_user_lat_without_user_lng(self, apple_client: AppleMapsClient):
        with pytest.raises(AssertionError, match="lat and lng must both"):
            apple_client.search(query="coffee", user_lat=37.334)

    def test_lat_lng_to_apple_str_requires_both(self):
        with pytest.raises(AssertionError, match="lat and lng must both"):
            _lat_lng_to_apple_str(lat=37.334)

        with pytest.raises(AssertionError, match="lat and lng must both"):
            _lat_lng_to_apple_str(lng=-122.009)

        assert _lat_lng_to_apple_str() is None
        assert _lat_lng_to_apple_str(lat=37.334, lng=-122.009) == "37.334,-122.009"

    def test_search_with_region(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        region = MapRegion(
            northLatitude=37.5,
            eastLongitude=-121.7,
            southLatitude=37.1,
            westLongitude=-122.5,
        )
        apple_client.search(
            query="coffee",
            search_region=region,
            search_region_priority=SearchRegionPriority.required,
        )

        assert route.called
        request = route.calls.last.request
        assert "searchRegion=37.5" in str(request.url)
        assert "-121.7" in str(request.url)
        assert "37.1" in str(request.url)
        assert "-122.5" in str(request.url)
        assert "searchRegionPriority=required" in str(request.url)

    def test_search_empty_query(self, apple_client: AppleMapsClient):
        with pytest.raises(ValueError, match="query must be provided"):
            apple_client.search(query="")

    def test_search_with_page_token_only(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/search").respond(
            json=SAMPLE_SEARCH_RESPONSE
        )

        apple_client.search(page_token="opaque-token")

        assert route.called
        request = route.calls.last.request
        assert "pageToken=opaque-token" in str(request.url)
        assert "q=" not in str(request.url)
        assert "enablePagination" not in str(request.url)


class TestAutocomplete:
    def test_autocomplete_success(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/searchAutocomplete").respond(
            json=SAMPLE_AUTOCOMPLETE_RESPONSE
        )

        result = apple_client.autocomplete(query="1 Apple Par")

        assert isinstance(result, SearchAutocompleteResponse)
        assert len(result.results) == 1
        assert result.results[0].completionUrl is not None

    def test_autocomplete_with_country_filter(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get(
            "https://maps-api.apple.com/v1/searchAutocomplete"
        ).respond(json=SAMPLE_AUTOCOMPLETE_RESPONSE)

        apple_client.autocomplete(
            query="1 Apple",
            limit_to_countries="US",
            result_type_filter="Address",
        )

        assert route.called
        request = route.calls.last.request
        assert "limitToCountries=US" in str(request.url)
        assert "resultTypeFilter=Address" in str(request.url)

    def test_autocomplete_with_lat_lng(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get(
            "https://maps-api.apple.com/v1/searchAutocomplete"
        ).respond(json=SAMPLE_AUTOCOMPLETE_RESPONSE)

        apple_client.autocomplete(query="1 Apple", lat=37.334, lng=-122.009)

        assert route.called
        request = route.calls.last.request
        assert "searchLocation=37.334" in str(request.url)
        assert "-122.009" in str(request.url)

    def test_autocomplete_empty_query(self, apple_client: AppleMapsClient):
        with pytest.raises(ValueError, match="query must be provided"):
            apple_client.autocomplete(query="")


class TestAuthentication:
    def test_bearer_token_sent(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        route = httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        apple_client.geocode("test")

        assert route.called
        request = route.calls.last.request
        assert request.headers["Authorization"] == "Bearer test_access_token"

    def test_token_cached(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        token_route = mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            json=SAMPLE_GEOCODE_RESPONSE
        )

        apple_client.geocode("test1")
        apple_client.geocode("test2")

        # /v1/token should only be called once due to caching
        assert token_route.call_count == 1

    def test_create_token(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        token = apple_client.create_token()
        assert token == "test_access_token"

    def test_create_mapkit_token_returns_jwt(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        token = apple_client.create_mapkit_token()
        # must be the raw JWT, not the exchanged access token — no /v1/token call
        assert token == "test_jwt"
        assert not httpx2_mock.calls

    def test_create_mapkit_token_default_ttl(self, monkeypatch: pytest.MonkeyPatch):
        client = AppleMapsClient(
            team_id="TEAM123456",
            key_id="KEY1234567",
            private_key=TEST_PRIVATE_KEY,
        )
        captured: dict[str, int] = {}

        def capture_jwt(*, ttl_seconds: int = 0) -> str:
            captured["ttl_seconds"] = ttl_seconds
            return "test_jwt"

        monkeypatch.setattr(client, "_create_jwt", capture_jwt)
        client.create_mapkit_token()
        assert captured["ttl_seconds"] == 60 * 60

    def test_create_mapkit_token_custom_ttl(self, monkeypatch: pytest.MonkeyPatch):
        client = AppleMapsClient(
            team_id="TEAM123456",
            key_id="KEY1234567",
            private_key=TEST_PRIVATE_KEY,
        )
        captured: dict[str, int] = {}

        def capture_jwt(*, ttl_seconds: int = 0) -> str:
            captured["ttl_seconds"] = ttl_seconds
            return "test_jwt"

        monkeypatch.setattr(client, "_create_jwt", capture_jwt)
        client.create_mapkit_token(ttl_seconds=2 * 60 * 60)
        assert captured["ttl_seconds"] == 2 * 60 * 60


class TestErrorHandling:
    def test_http_error_raises(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            500, json={"error": "Server error"}
        )

        with pytest.raises(httpx2.HTTPStatusError):
            apple_client.geocode("test")

    def test_payment_required_no_retry(
        self, apple_client: AppleMapsClient, httpx2_mock: respx.Router
    ):
        mock_token(httpx2_mock)
        httpx2_mock.get("https://maps-api.apple.com/v1/geocode").respond(
            402, json={"error": "Payment required"}
        )

        with pytest.raises(httpx2.HTTPStatusError) as exc_info:
            apple_client.geocode("test")

        assert exc_info.value.response.status_code == 402
