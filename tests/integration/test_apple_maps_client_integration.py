"""Integration tests for AppleMapsClient against the real Apple Maps API.

These tests require the following environment variables to be set:
- APPLE_MAPS_TEAM_ID
- APPLE_MAPS_KEY_ID
- APPLE_MAPS_P8_KEY
"""

import pytest

from apple_maps_api import AppleMapsClient, geocode_coordinates, geocode_postal_code


@pytest.fixture
def apple_client() -> AppleMapsClient:
    return AppleMapsClient.from_env()


# TODO too many classes here, let's use top-level test functions instead
class TestAppleMapsClientIntegration:
    def test_geocode(self, apple_client: AppleMapsClient):
        result = apple_client.geocode("1 Apple Park Way, Cupertino, CA")

        assert len(result.results) > 0
        place = result.results[0]
        assert place.structuredAddress is not None
        assert place.structuredAddress.locality is not None
        assert "Cupertino" in place.structuredAddress.locality

    def test_reverse_geocode(self, apple_client: AppleMapsClient):
        result = apple_client.reverse_geocode((37.3349, -122.0090))

        assert len(result.results) > 0
        place = result.results[0]
        assert place.countryCode == "US"

    def test_search(self, apple_client: AppleMapsClient):
        result = apple_client.search(
            query="Apple Park",
            near="37.3349,-122.0090",
        )

        assert len(result.results) > 0
        assert result.results[0].name is not None

    def test_autocomplete(self, apple_client: AppleMapsClient):
        result = apple_client.autocomplete(
            query="1 Apple Par",
            limit_to_countries="US",
        )

        assert len(result.results) > 0
        assert result.results[0].completionUrl is not None

    def test_create_token(self, apple_client: AppleMapsClient):
        token = apple_client.create_token()
        assert isinstance(token, str)
        assert len(token) > 0


class TestHelpersIntegration:
    def test_geocode_postal_code(self, apple_client: AppleMapsClient):
        result = geocode_postal_code(apple_client, postal_code="95014", country="US")

        assert result is not None
        assert result.city is not None
        assert result.state_code is not None

    def test_geocode_coordinates(self, apple_client: AppleMapsClient):
        result = geocode_coordinates(apple_client, lat=37.3349, lon=-122.0090)

        assert result is not None
        assert result.country_code == "US"
