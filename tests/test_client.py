"""Tests for AppleMapsClient."""

import httpx
import pytest
import respx

from apple_maps_api import AppleMapsClient
from apple_maps_api.models import (
    Location,
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
    monkeypatch.setattr(client, "_create_jwt", lambda: "test_jwt")
    return client


def mock_token() -> respx.Route:
    """Set up mock for /v1/token endpoint."""
    return respx.get("https://maps-api.apple.com/v1/token").mock(
        return_value=httpx.Response(200, json=TOKEN_RESPONSE)
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


class TestGeocode:
    @respx.mock
    def test_geocode_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
        )

        result = apple_client.geocode("1 Apple Park Way, Cupertino, CA")

        assert isinstance(result, PlaceResults)
        assert len(result.results) == 1
        assert result.results[0].structuredAddress is not None
        assert result.results[0].structuredAddress.locality == "Cupertino"

    @respx.mock
    def test_geocode_with_params(self, apple_client: AppleMapsClient):
        mock_token()
        route = respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
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
    @respx.mock
    def test_reverse_geocode_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/reverseGeocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
        )

        result = apple_client.reverse_geocode((37.3349, -122.0090))

        assert isinstance(result, PlaceResults)
        assert len(result.results) == 1

    @respx.mock
    def test_reverse_geocode_with_location(self, apple_client: AppleMapsClient):
        mock_token()
        route = respx.get("https://maps-api.apple.com/v1/reverseGeocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
        )

        apple_client.reverse_geocode(Location(latitude=37.3349, longitude=-122.0090))

        assert route.called
        request = route.calls.last.request
        assert "loc=37.3349" in str(request.url)


class TestSearch:
    @respx.mock
    def test_search_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/search").mock(
            return_value=httpx.Response(200, json=SAMPLE_SEARCH_RESPONSE)
        )

        result = apple_client.search(query="Apple Park")

        assert isinstance(result, SearchResponse)
        assert len(result.results) == 1
        assert result.results[0].poiCategory == "Landmark"
        assert result.displayMapRegion is not None

    @respx.mock
    def test_search_with_params(self, apple_client: AppleMapsClient):
        mock_token()
        route = respx.get("https://maps-api.apple.com/v1/search").mock(
            return_value=httpx.Response(200, json=SAMPLE_SEARCH_RESPONSE)
        )

        apple_client.search(
            query="coffee",
            near="37.334,-122.009",
            categories="Cafe",
            limit_to_countries="US",
        )

        assert route.called
        request = route.calls.last.request
        assert "q=coffee" in str(request.url)
        assert "searchLocation=37.334" in str(request.url)
        assert "includePoiCategories=Cafe" in str(request.url)
        assert "limitToCountries=US" in str(request.url)

    def test_search_empty_query(self, apple_client: AppleMapsClient):
        with pytest.raises(ValueError, match="query must be provided"):
            apple_client.search(query="")


class TestAutocomplete:
    @respx.mock
    def test_autocomplete_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/searchAutocomplete").mock(
            return_value=httpx.Response(200, json=SAMPLE_AUTOCOMPLETE_RESPONSE)
        )

        result = apple_client.autocomplete(query="1 Apple Par")

        assert isinstance(result, SearchAutocompleteResponse)
        assert len(result.results) == 1
        assert result.results[0].completionUrl is not None

    @respx.mock
    def test_autocomplete_with_country_filter(self, apple_client: AppleMapsClient):
        mock_token()
        route = respx.get("https://maps-api.apple.com/v1/searchAutocomplete").mock(
            return_value=httpx.Response(200, json=SAMPLE_AUTOCOMPLETE_RESPONSE)
        )

        apple_client.autocomplete(
            query="1 Apple",
            limit_to_countries="US",
            result_type_filter="Address",
        )

        assert route.called
        request = route.calls.last.request
        assert "limitToCountries=US" in str(request.url)
        assert "resultTypeFilter=Address" in str(request.url)

    def test_autocomplete_empty_query(self, apple_client: AppleMapsClient):
        with pytest.raises(ValueError, match="query must be provided"):
            apple_client.autocomplete(query="")


class TestAuthentication:
    @respx.mock
    def test_bearer_token_sent(self, apple_client: AppleMapsClient):
        mock_token()
        route = respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
        )

        apple_client.geocode("test")

        assert route.called
        request = route.calls.last.request
        assert request.headers["Authorization"] == "Bearer test_access_token"

    @respx.mock
    def test_token_cached(self, apple_client: AppleMapsClient):
        token_route = mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_GEOCODE_RESPONSE)
        )

        apple_client.geocode("test1")
        apple_client.geocode("test2")

        # /v1/token should only be called once due to caching
        assert token_route.call_count == 1

    @respx.mock
    def test_create_token(self, apple_client: AppleMapsClient):
        mock_token()
        token = apple_client.create_token()
        assert token == "test_access_token"

    @respx.mock
    def test_create_mapkit_token_returns_jwt(self, apple_client: AppleMapsClient):
        token_route = mock_token()
        token = apple_client.create_mapkit_token()
        # must be the raw JWT, not the exchanged access token
        assert token == "test_jwt"
        assert token_route.call_count == 0


class TestErrorHandling:
    @respx.mock
    def test_http_error_raises(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(500, json={"error": "Server error"})
        )

        with pytest.raises(httpx.HTTPStatusError):
            apple_client.geocode("test")

    @respx.mock
    def test_payment_required_no_retry(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(402, json={"error": "Payment required"})
        )

        with pytest.raises(httpx.HTTPStatusError) as exc_info:
            apple_client.geocode("test")

        assert exc_info.value.response.status_code == 402
