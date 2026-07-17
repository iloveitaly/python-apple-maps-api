"""Tests for Pydantic models."""

import pytest
from pydantic import ValidationError

from apple_maps_api.models import (
    AutocompleteResult,
    GeocodeResult,
    Location,
    MapRegion,
    Place,
    PlaceResults,
    PoiCategory,
    SearchAutocompleteResponse,
    SearchPlace,
    SearchResponse,
    StructuredAddress,
    TokenResponse,
)


class TestLocation:
    def test_valid_location(self):
        loc = Location(latitude=37.334, longitude=-122.009)
        assert loc.latitude == 37.334
        assert loc.longitude == -122.009

    def test_missing_field(self):
        with pytest.raises(ValidationError):
            Location(latitude=37.334)  # type: ignore[call-arg]


class TestStructuredAddress:
    def test_full_address(self):
        addr = StructuredAddress(
            administrativeArea="California",
            administrativeAreaCode="CA",
            locality="Cupertino",
            postCode="95014",
            fullThoroughfare="1 Apple Park Way",
            thoroughfare="Apple Park Way",
            subThoroughfare="1",
            subLocality="",
            areasOfInterest=["Apple Park"],
            dependentLocalities=[],
        )

        assert addr.locality == "Cupertino"
        assert addr.administrativeAreaCode == "CA"
        assert addr.postCode == "95014"
        assert addr.fullThoroughfare == "1 Apple Park Way"

    def test_minimal_address(self):
        addr = StructuredAddress()
        assert addr.locality is None
        assert addr.postCode is None


class TestMapRegion:
    def test_valid_region(self):
        region = MapRegion(
            northLatitude=37.5,
            southLatitude=37.1,
            eastLongitude=-121.7,
            westLongitude=-122.5,
        )

        assert region.northLatitude == 37.5
        assert region.southLatitude == 37.1


class TestPlace:
    def test_full_place(self):
        place = Place(
            id="abc123",
            name="Apple Park",
            coordinate=Location(latitude=37.334, longitude=-122.009),
            formattedAddressLines=["1 Apple Park Way", "Cupertino, CA 95014"],
            structuredAddress=StructuredAddress(locality="Cupertino"),
            country="United States",
            countryCode="US",
        )

        assert place.name == "Apple Park"
        assert place.coordinate is not None
        assert place.coordinate.latitude == 37.334
        assert place.countryCode == "US"

    def test_minimal_place(self):
        place = Place()
        assert place.name is None
        assert place.coordinate is None
        assert place.formattedAddressLines is None


class TestSearchPlace:
    def test_with_poi_category(self):
        place = SearchPlace(
            name="AMC Theaters",
            poiCategory="MovieTheater",
            coordinate=Location(latitude=37.334, longitude=-122.009),
        )

        assert place.poiCategory == PoiCategory.MovieTheater
        assert place.name == "AMC Theaters"

    def test_unknown_poi_category_fails(self):
        with pytest.raises(ValidationError):
            SearchPlace(name="Somewhere", poiCategory="NotARealCategory")

    def test_inherits_place_fields(self):
        place = SearchPlace(
            name="Test",
            countryCode="US",
        )

        assert place.countryCode == "US"
        assert place.poiCategory is None


class TestPlaceResults:
    def test_valid_results(self):
        results = PlaceResults(
            results=[
                Place(name="Apple Park", countryCode="US"),
            ]
        )

        assert len(results.results) == 1
        assert results.results[0].name == "Apple Park"

    def test_empty_results(self):
        results = PlaceResults(results=[])
        assert len(results.results) == 0


class TestSearchResponse:
    def test_valid_response(self):
        resp = SearchResponse(
            results=[
                SearchPlace(name="Apple Park", poiCategory="Landmark"),
            ],
            displayMapRegion=MapRegion(
                northLatitude=37.5,
                southLatitude=37.1,
                eastLongitude=-121.7,
                westLongitude=-122.5,
            ),
        )

        assert len(resp.results) == 1
        assert resp.displayMapRegion is not None

    def test_without_map_region(self):
        resp = SearchResponse(results=[])
        assert resp.displayMapRegion is None


class TestAutocompleteResult:
    def test_valid_result(self):
        result = AutocompleteResult(
            completionUrl="/v1/search?q=1+Apple+Park&metadata=abc",
            displayLines=["1 Apple Park Way", "Cupertino, CA"],
            location=Location(latitude=37.334, longitude=-122.009),
            structuredAddress=StructuredAddress(locality="Cupertino"),
        )

        assert result.completionUrl is not None
        assert result.displayLines is not None
        assert len(result.displayLines) == 2

    def test_minimal_result(self):
        result = AutocompleteResult()
        assert result.completionUrl is None
        assert result.displayLines is None


class TestSearchAutocompleteResponse:
    def test_valid_response(self):
        resp = SearchAutocompleteResponse(
            results=[
                AutocompleteResult(displayLines=["1 Apple Park Way"]),
            ]
        )

        assert len(resp.results) == 1


class TestTokenResponse:
    def test_valid_token(self):
        token = TokenResponse(accessToken="abc123", expiresInSeconds=1800)
        assert token.accessToken == "abc123"
        assert token.expiresInSeconds == 1800


class TestGeocodeResult:
    def test_valid_full(self):
        result = GeocodeResult(
            lat=37.334,
            lon=-122.009,
            address1="1 Apple Park Way",
            address2=None,
            postal_code="95014",
            city="Cupertino",
            state_code="CA",
            country_code="US",
            formatted_address="1 Apple Park Way, Cupertino, CA 95014",
        )

        assert result.lat == 37.334
        assert result.lon == -122.009
        assert result.address1 == "1 Apple Park Way"
        assert result.country_code == "US"

    def test_with_nulls(self):
        result = GeocodeResult(
            lat=37.334,
            lon=-122.009,
            postal_code=None,
            city=None,
            state_code=None,
            formatted_address=None,
        )

        assert result.city is None

    def test_missing_required_field(self):
        with pytest.raises(ValidationError):
            GeocodeResult(  # type: ignore[call-arg]
                lat=37.334,
                postal_code="95014",
                city="Cupertino",
                state_code="CA",
                formatted_address="Cupertino, CA",
            )
