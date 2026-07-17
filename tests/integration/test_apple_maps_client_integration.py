"""Integration tests for AppleMapsClient against the real Apple Maps API.

These tests require the following environment variables to be set:
- APPLE_MAPS_TEAM_ID
- APPLE_MAPS_KEY_ID
- APPLE_MAPS_P8_KEY
"""

import pytest

from apple_maps_api import (
    AddressCategory,
    AppleMapsClient,
    Location,
    MapRegion,
    PoiCategory,
    SearchACResultType,
    SearchRegionPriority,
    SearchResultType,
    geocode_coordinates,
    geocode_postal_code,
)

# Stable fixtures around Apple Park / Cupertino.
APPLE_PARK_LAT = 37.3349
APPLE_PARK_LNG = -122.0090
APPLE_PARK_ADDRESS = "1 Apple Park Way, Cupertino, CA"
CUPERTINO_REGION = MapRegion(
    northLatitude=37.36,
    eastLongitude=-121.95,
    southLatitude=37.30,
    westLongitude=-122.08,
)


@pytest.fixture
def apple_client() -> AppleMapsClient:
    return AppleMapsClient.from_env()


def test_create_token(apple_client: AppleMapsClient):
    token = apple_client.create_token()
    assert isinstance(token, str)
    assert len(token) > 0


def test_token_reuse_across_calls(apple_client: AppleMapsClient):
    """Two API calls on one client succeed (live token cache path)."""
    first = apple_client.geocode(APPLE_PARK_ADDRESS)
    second = apple_client.reverse_geocode(lat=APPLE_PARK_LAT, lng=APPLE_PARK_LNG)
    assert len(first.results) > 0
    assert len(second.results) > 0


def test_geocode(apple_client: AppleMapsClient):
    result = apple_client.geocode(APPLE_PARK_ADDRESS)

    assert len(result.results) > 0
    place = result.results[0]
    assert place.coordinate is not None
    assert isinstance(place.coordinate.latitude, float)
    assert isinstance(place.coordinate.longitude, float)
    assert place.structuredAddress is not None
    assert place.structuredAddress.locality is not None
    assert "Cupertino" in place.structuredAddress.locality


def test_geocode_with_lat_lng_and_country(apple_client: AppleMapsClient):
    result = apple_client.geocode(
        APPLE_PARK_ADDRESS,
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        limit_to_countries=["US"],
    )

    assert len(result.results) > 0
    assert result.results[0].countryCode == "US"


def test_geocode_with_user_location(apple_client: AppleMapsClient):
    result = apple_client.geocode(
        APPLE_PARK_ADDRESS,
        user_lat=APPLE_PARK_LAT,
        user_lng=APPLE_PARK_LNG,
    )

    assert len(result.results) > 0
    assert result.results[0].coordinate is not None


def test_geocode_with_search_region(apple_client: AppleMapsClient):
    result = apple_client.geocode(
        "Apple Park",
        search_region=CUPERTINO_REGION,
    )

    assert len(result.results) > 0


def test_reverse_geocode(apple_client: AppleMapsClient):
    result = apple_client.reverse_geocode(lat=APPLE_PARK_LAT, lng=APPLE_PARK_LNG)

    assert len(result.results) > 0
    place = result.results[0]
    assert place.countryCode == "US"
    assert place.coordinate is not None
    assert place.structuredAddress is not None


def test_reverse_geocode_with_lang(apple_client: AppleMapsClient):
    result = apple_client.reverse_geocode(
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        lang="en-US",
    )

    assert len(result.results) > 0
    assert result.results[0].countryCode == "US"


def test_search(apple_client: AppleMapsClient):
    result = apple_client.search(
        query="Apple Park",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
    )

    assert len(result.results) > 0
    place = result.results[0]
    assert place.name is not None
    if result.displayMapRegion is not None:
        assert isinstance(result.displayMapRegion.northLatitude, float)


def test_search_with_poi_category_parses_enum(apple_client: AppleMapsClient):
    result = apple_client.search(
        query="coffee",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        categories=[PoiCategory.Cafe],
    )

    assert len(result.results) > 0
    categorized = [p for p in result.results if p.poiCategory is not None]
    assert categorized, "expected at least one result with poiCategory"
    for place in categorized:
        assert isinstance(place.poiCategory, PoiCategory)


def test_search_with_user_location(apple_client: AppleMapsClient):
    result = apple_client.search(
        query="Apple Park",
        user_lat=APPLE_PARK_LAT,
        user_lng=APPLE_PARK_LNG,
    )

    assert len(result.results) > 0
    assert result.results[0].name is not None


def test_search_with_search_region(apple_client: AppleMapsClient):
    result = apple_client.search(
        query="coffee",
        search_region=CUPERTINO_REGION,
        search_region_priority=SearchRegionPriority.required,
    )

    assert len(result.results) > 0


def test_search_with_result_type_and_address_categories(
    apple_client: AppleMapsClient,
):
    result = apple_client.search(
        query="Cupertino",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        result_type_filter=[SearchResultType.address],
        include_address_categories=[AddressCategory.Locality],
    )

    assert len(result.results) > 0


def test_search_pagination(apple_client: AppleMapsClient):
    first = apple_client.search(
        query="restaurant",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        enable_pagination=True,
    )

    assert len(first.results) > 0
    assert first.paginationInfo is not None
    assert first.paginationInfo.nextPageToken
    assert first.paginationInfo.totalResults is not None

    # Apple requires pageToken alone on follow-up pages (no q / filters).
    second = apple_client.search(page_token=first.paginationInfo.nextPageToken)
    assert len(second.results) > 0


def test_autocomplete(apple_client: AppleMapsClient):
    result = apple_client.autocomplete(
        query="1 Apple Par",
        limit_to_countries=["US"],
    )

    assert len(result.results) > 0
    assert result.results[0].completionUrl is not None


def test_autocomplete_with_lat_lng(apple_client: AppleMapsClient):
    result = apple_client.autocomplete(
        query="1 Apple Par",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        limit_to_countries=["US"],
    )

    assert len(result.results) > 0
    suggestion = result.results[0]
    assert suggestion.completionUrl is not None
    if suggestion.location is not None:
        assert isinstance(suggestion.location, Location)


def test_autocomplete_with_poi_categories(apple_client: AppleMapsClient):
    result = apple_client.autocomplete(
        query="cafe",
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
        include_poi_categories=[PoiCategory.Cafe],
        result_type_filter=[SearchACResultType.poi],
    )

    assert len(result.results) > 0


def test_search_completion_from_autocomplete(apple_client: AppleMapsClient):
    suggestions = apple_client.autocomplete(
        query="1 Apple Par",
        limit_to_countries=["US"],
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
    )
    assert len(suggestions.results) > 0

    hit = next(r for r in suggestions.results if r.completionUrl)
    resolved = apple_client.search_completion(hit, lang="en-US")

    assert len(resolved.results) > 0
    assert (
        resolved.results[0].name is not None
        or resolved.results[0].coordinate is not None
    )


def test_search_completion_from_url_string(apple_client: AppleMapsClient):
    suggestions = apple_client.autocomplete(
        query="1 Apple Par",
        limit_to_countries=["US"],
        lat=APPLE_PARK_LAT,
        lng=APPLE_PARK_LNG,
    )
    url = next(r.completionUrl for r in suggestions.results if r.completionUrl)
    resolved = apple_client.search_completion(url)

    assert len(resolved.results) > 0


def test_geocode_postal_code(apple_client: AppleMapsClient):
    result = geocode_postal_code(apple_client, postal_code="95014", country="US")

    assert result is not None
    assert result.city is not None
    assert result.state_code is not None


def test_geocode_coordinates(apple_client: AppleMapsClient):
    result = geocode_coordinates(apple_client, lat=APPLE_PARK_LAT, lon=APPLE_PARK_LNG)

    assert result is not None
    assert result.country_code == "US"
