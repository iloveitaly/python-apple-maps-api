"""apple-maps-api: A Python client for the Apple Maps Server API.

This package provides a type-safe, production-ready client for interacting with
Apple Maps geocoding, reverse geocoding, search, and autocomplete APIs.
"""

from .client import AppleMapsClient
from .helpers import geocode_coordinates, geocode_postal_code
from .models import (
    AddressCategory,
    AutocompleteResult,
    GeocodeResult,
    Location,
    MapRegion,
    Place,
    PlaceResults,
    PoiCategory,
    SearchACResultType,
    SearchAutocompleteResponse,
    SearchPlace,
    SearchRegionPriority,
    SearchResponse,
    SearchResultType,
    StructuredAddress,
    TokenResponse,
)
from .version import __version__

__all__ = [
    "__version__",
    "AppleMapsClient",
    "geocode_coordinates",
    "geocode_postal_code",
    "AddressCategory",
    "AutocompleteResult",
    "GeocodeResult",
    "Location",
    "MapRegion",
    "Place",
    "PlaceResults",
    "PoiCategory",
    "SearchACResultType",
    "SearchAutocompleteResponse",
    "SearchPlace",
    "SearchRegionPriority",
    "SearchResponse",
    "SearchResultType",
    "StructuredAddress",
    "TokenResponse",
]
