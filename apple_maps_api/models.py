"""Pydantic models for Apple Maps Server API responses.

Model names and field names match Apple's official API documentation exactly.
Docstrings explain what each field represents in familiar terms.

See: https://developer.apple.com/documentation/applemapsserverapi
"""

from enum import StrEnum

from pydantic import BaseModel


class AddressCategory(StrEnum):
    Country = "Country"
    AdministrativeArea = "AdministrativeArea"
    SubAdministrativeArea = "SubAdministrativeArea"
    Locality = "Locality"
    SubLocality = "SubLocality"
    PostalCode = "PostalCode"


class PoiCategory(StrEnum):
    Airport = "Airport"
    AirportGate = "AirportGate"
    AirportTerminal = "AirportTerminal"
    AmusementPark = "AmusementPark"
    AnimalService = "AnimalService"
    Aquarium = "Aquarium"
    ATM = "ATM"
    AutomotiveRepair = "AutomotiveRepair"
    Bakery = "Bakery"
    Bank = "Bank"
    Baseball = "Baseball"
    Basketball = "Basketball"
    Beach = "Beach"
    Beauty = "Beauty"
    Bowling = "Bowling"
    Brewery = "Brewery"
    Cafe = "Cafe"
    Campground = "Campground"
    CarRental = "CarRental"
    Castle = "Castle"
    ConventionCenter = "ConventionCenter"
    Distillery = "Distillery"
    EVCharger = "EVCharger"
    Fairground = "Fairground"
    FireStation = "FireStation"
    Fishing = "Fishing"
    FitnessCenter = "FitnessCenter"
    FoodMarket = "FoodMarket"
    Fortress = "Fortress"
    GasStation = "GasStation"
    GoKart = "GoKart"
    Golf = "Golf"
    Hiking = "Hiking"
    Hospital = "Hospital"
    Hotel = "Hotel"
    Kayaking = "Kayaking"
    Landmark = "Landmark"
    Laundry = "Laundry"
    Library = "Library"
    Mailbox = "Mailbox"
    Marina = "Marina"
    MiniGolf = "MiniGolf"
    MovieTheater = "MovieTheater"
    Museum = "Museum"
    MusicVenue = "MusicVenue"
    NationalMonument = "NationalMonument"
    NationalPark = "NationalPark"
    Nightlife = "Nightlife"
    Park = "Park"
    Parking = "Parking"
    Pharmacy = "Pharmacy"
    Planetarium = "Planetarium"
    Playground = "Playground"
    Police = "Police"
    PostOffice = "PostOffice"
    PublicTransport = "PublicTransport"
    ReligiousSite = "ReligiousSite"
    Restaurant = "Restaurant"
    Restroom = "Restroom"
    RockClimbing = "RockClimbing"
    RVPark = "RVPark"
    School = "School"
    SkatePark = "SkatePark"
    Skating = "Skating"
    Skiing = "Skiing"
    Soccer = "Soccer"
    Spa = "Spa"
    Stadium = "Stadium"
    Store = "Store"
    Surfing = "Surfing"
    Swimming = "Swimming"
    Tennis = "Tennis"
    Theater = "Theater"
    University = "University"
    Volleyball = "Volleyball"
    Winery = "Winery"
    Zoo = "Zoo"


class SearchResultType(StrEnum):
    """Result type filter for /v1/search."""
    poi = "poi"
    address = "address"
    physicalFeature = "physicalFeature"
    pointOfInterest = "pointOfInterest"


class SearchACResultType(StrEnum):
    """Result type filter for /v1/searchAutocomplete."""
    poi = "poi"
    address = "address"
    physicalFeature = "physicalFeature"
    pointOfInterest = "pointOfInterest"
    query = "query"


class Location(BaseModel):
    """A coordinate pair from Apple Maps API.

    latitude: north-south position (e.g. 37.334)
    longitude: east-west position (e.g. -122.009)
    """

    latitude: float
    longitude: float


class StructuredAddress(BaseModel):
    """Detailed address components of a place.

    Apple uses different terminology than most geocoding APIs:
    - locality = city
    - administrativeArea = state/province name
    - administrativeAreaCode = state/province short code (e.g. "NY")
    - subAdministrativeArea = county name
    - postCode = postal/ZIP code
    - fullThoroughfare = full street address (number + street, e.g. "841 Broadway")
    - thoroughfare = street name (e.g. "Broadway")
    - subThoroughfare = street/house number (e.g. "841")
    - subLocality = neighborhood or area within the city
    - areasOfInterest = common names for the surrounding area
    - dependentLocalities = neighborhood names
    """

    administrativeArea: str | None = None
    administrativeAreaCode: str | None = None
    subAdministrativeArea: str | None = None
    areasOfInterest: list[str] | None = None
    dependentLocalities: list[str] | None = None
    fullThoroughfare: str | None = None
    locality: str | None = None
    postCode: str | None = None
    subLocality: str | None = None
    subThoroughfare: str | None = None
    thoroughfare: str | None = None


class MapRegion(BaseModel):
    """A rectangular bounding box on a map.

    Expressed as south-west and north-east corners.
    """

    eastLongitude: float
    northLatitude: float
    southLatitude: float
    westLongitude: float


class Place(BaseModel):
    """A place returned by geocode, reverseGeocode, or place lookup endpoints.

    coordinate: lat/lng of the place
    formattedAddressLines: human-readable address lines (e.g. ["841 Broadway", "New York, NY 10003"])
    structuredAddress: parsed address components
    displayMapRegion: suggested map viewport for displaying this place
    """

    id: str | None = None
    name: str | None = None
    coordinate: Location | None = None
    formattedAddressLines: list[str] | None = None
    structuredAddress: StructuredAddress | None = None
    country: str | None = None
    countryCode: str | None = None
    displayMapRegion: MapRegion | None = None
    alternateIds: list[str] | None = None


class SearchPlace(Place):
    """Extended Place returned by /v1/search with POI category info.

    poiCategory: point-of-interest category (e.g. "Restaurant", "MovieTheater")
    """

    poiCategory: str | None = None


class PlaceResults(BaseModel):
    """Response from /v1/geocode and /v1/reverseGeocode.

    results: list of Place objects matching the query
    """

    results: list[Place]


class SearchResponse(BaseModel):
    """Response from /v1/search.

    results: list of SearchPlace objects with optional POI category
    displayMapRegion: suggested map viewport encompassing all results
    """

    results: list[SearchPlace]
    displayMapRegion: MapRegion | None = None


class AutocompleteResult(BaseModel):
    """A single autocomplete suggestion from /v1/searchAutocomplete.

    completionUrl: relative URL to /v1/search to fetch full details for this suggestion
    displayLines: raw text lines Apple returns — use completionTitle / completionSubtitle instead
    location: approximate coordinate of the suggestion
    structuredAddress: parsed address components if available
    """

    completionUrl: str | None = None
    displayLines: list[str] | None = None
    location: Location | None = None
    structuredAddress: StructuredAddress | None = None

    @property
    def completionTitle(self) -> str | None:
        """Primary display text (e.g. place name or street address)."""
        return self.displayLines[0] if self.displayLines else None

    @property
    def completionSubtitle(self) -> str | None:
        """Secondary display text (e.g. city, state)."""
        return self.displayLines[1] if self.displayLines and len(self.displayLines) > 1 else None


class SearchAutocompleteResponse(BaseModel):
    """Response from /v1/searchAutocomplete.

    results: list of autocomplete suggestions
    """

    results: list[AutocompleteResult]


class TokenResponse(BaseModel):
    """Response from /v1/token.

    accessToken: short-lived Bearer token for API requests
    expiresInSeconds: token lifetime (typically 1800 = 30 minutes)
    """

    accessToken: str
    expiresInSeconds: int


class GeocodeResult(BaseModel):
    """Provider-agnostic geocode result.

    Identical to radar-mapping-api's GeocodeResult for drop-in replacement.
    This abstraction allows swapping Apple Maps for Radar without changing consuming code.
    """

    lat: float
    lon: float
    address1: str | None = None
    address2: str | None = None
    postal_code: str | None
    city: str | None
    state_code: str | None
    country_code: str | None = None
    formatted_address: str | None
