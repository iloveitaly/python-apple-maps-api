"""Tests for helper functions."""

import httpx
import pytest
import respx

from apple_maps_api import AppleMapsClient, geocode_coordinates, geocode_postal_code
from apple_maps_api.models import GeocodeResult

from tests.constants import (
    SAMPLE_POSTAL_GEOCODE_RESPONSE,
    SAMPLE_REVERSE_GEOCODE_RESPONSE,
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


# TODO is there a good reason we shouldn't make this a fixture? or at least mock across TestGeocodePostalCode
def mock_token() -> respx.Route:
    return respx.get("https://maps-api.apple.com/v1/token").mock(
        return_value=httpx.Response(200, json=TOKEN_RESPONSE)
    )


class TestGeocodePostalCode:
    @respx.mock
    def test_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_POSTAL_GEOCODE_RESPONSE)
        )

        result = geocode_postal_code(apple_client, postal_code="95014", country="US")

        assert result is not None
        assert isinstance(result, GeocodeResult)
        assert result.lat == 37.318
        assert result.lon == -122.045
        assert result.postal_code == "95014"
        assert result.city == "Cupertino"
        assert result.state_code == "CA"
        assert result.country_code == "US"
        assert result.formatted_address == "Cupertino, CA 95014"

    @respx.mock
    def test_no_results(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json={"results": []})
        )

        result = geocode_postal_code(apple_client, postal_code="00000", country="US")

        assert result is None

    @respx.mock
    def test_multiple_results(self, apple_client: AppleMapsClient):
        mock_token()
        multiple_response = {
            "results": [
                SAMPLE_POSTAL_GEOCODE_RESPONSE["results"][0],
                SAMPLE_POSTAL_GEOCODE_RESPONSE["results"][0],
            ]
        }
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=multiple_response)
        )

        result = geocode_postal_code(apple_client, postal_code="95014", country="US")

        assert result is not None

    @respx.mock
    def test_missing_coordinate_returns_none(self, apple_client: AppleMapsClient):
        mock_token()
        # place with no coordinate field
        response = {
            "results": [
                {
                    "name": "somewhere",
                    "structuredAddress": {"locality": "Cupertino"},
                    "countryCode": "US",
                }
            ]
        }
        respx.get("https://maps-api.apple.com/v1/geocode").mock(
            return_value=httpx.Response(200, json=response)
        )

        result = geocode_postal_code(apple_client, postal_code="99999", country="US")

        assert result is None


class TestGeocodeCoordinates:
    @respx.mock
    def test_success(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/reverseGeocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_REVERSE_GEOCODE_RESPONSE)
        )

        result = geocode_coordinates(apple_client, lat=37.3349, lon=-122.0090)

        assert result is not None
        assert isinstance(result, GeocodeResult)
        # preserves caller's coordinates
        assert result.lat == 37.3349
        assert result.lon == -122.0090
        assert result.postal_code == "95014"
        assert result.city == "Cupertino"
        assert result.state_code == "CA"
        assert result.country_code == "US"

    @respx.mock
    def test_no_results(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/reverseGeocode").mock(
            return_value=httpx.Response(200, json={"results": []})
        )

        result = geocode_coordinates(apple_client, lat=0.0, lon=0.0)

        assert result is None

    @respx.mock
    def test_with_street_address(self, apple_client: AppleMapsClient):
        mock_token()
        respx.get("https://maps-api.apple.com/v1/reverseGeocode").mock(
            return_value=httpx.Response(200, json=SAMPLE_REVERSE_GEOCODE_RESPONSE)
        )

        result = geocode_coordinates(apple_client, lat=37.3349, lon=-122.0090)

        assert result is not None
        assert result.address1 == "1 Apple Park Way"
        assert result.address2 is None
