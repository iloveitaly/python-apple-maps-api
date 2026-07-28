# apple_maps_api.models

.. py:module:: apple_maps_api.models

.. autoapi-nested-parse::

Pydantic models for Apple Maps Server API responses.

Model names and field names match Apple’s official API documentation exactly.
Docstrings explain what each field represents in familiar terms.

See: https://developer.apple.com/documentation/applemapsserverapi

## Classes

.. autoapisummary::

apple_maps_api.models.AddressCategory
apple_maps_api.models.PoiCategory
apple_maps_api.models.SearchResultType
apple_maps_api.models.SearchACResultType
apple_maps_api.models.SearchRegionPriority
apple_maps_api.models.Location
apple_maps_api.models.StructuredAddress
apple_maps_api.models.MapRegion
apple_maps_api.models.Place
apple_maps_api.models.SearchPlace
apple_maps_api.models.PlaceResults
apple_maps_api.models.PaginationInfo
apple_maps_api.models.SearchResponse
apple_maps_api.models.AutocompleteResult
apple_maps_api.models.SearchAutocompleteResponse
apple_maps_api.models.TokenResponse
apple_maps_api.models.GeocodeResult

## Module Contents

.. py:class:: AddressCategory

Bases: :py:obj:`enum.StrEnum`

Enum where members are also (and must be) strings

.. py:attribute:: Country
:value: ‘Country’

.. py:attribute:: AdministrativeArea
:value: ‘AdministrativeArea’

.. py:attribute:: SubAdministrativeArea
:value: ‘SubAdministrativeArea’

.. py:attribute:: Locality
:value: ‘Locality’

.. py:attribute:: SubLocality
:value: ‘SubLocality’

.. py:attribute:: PostalCode
:value: ‘PostalCode’

.. py:class:: PoiCategory

Bases: :py:obj:`enum.StrEnum`

Enum where members are also (and must be) strings

.. py:attribute:: Airport
:value: ‘Airport’

.. py:attribute:: AirportGate
:value: ‘AirportGate’

.. py:attribute:: AirportTerminal
:value: ‘AirportTerminal’

.. py:attribute:: AmusementPark
:value: ‘AmusementPark’

.. py:attribute:: AnimalService
:value: ‘AnimalService’

.. py:attribute:: Aquarium
:value: ‘Aquarium’

.. py:attribute:: ATM
:value: ‘ATM’

.. py:attribute:: AutomotiveRepair
:value: ‘AutomotiveRepair’

.. py:attribute:: Bakery
:value: ‘Bakery’

.. py:attribute:: Bank
:value: ‘Bank’

.. py:attribute:: Baseball
:value: ‘Baseball’

.. py:attribute:: Basketball
:value: ‘Basketball’

.. py:attribute:: Beach
:value: ‘Beach’

.. py:attribute:: Beauty
:value: ‘Beauty’

.. py:attribute:: Bowling
:value: ‘Bowling’

.. py:attribute:: Brewery
:value: ‘Brewery’

.. py:attribute:: Cafe
:value: ‘Cafe’

.. py:attribute:: Campground
:value: ‘Campground’

.. py:attribute:: CarRental
:value: ‘CarRental’

.. py:attribute:: Castle
:value: ‘Castle’

.. py:attribute:: ConventionCenter
:value: ‘ConventionCenter’

.. py:attribute:: Distillery
:value: ‘Distillery’

.. py:attribute:: EVCharger
:value: ‘EVCharger’

.. py:attribute:: Fairground
:value: ‘Fairground’

.. py:attribute:: FireStation
:value: ‘FireStation’

.. py:attribute:: Fishing
:value: ‘Fishing’

.. py:attribute:: FitnessCenter
:value: ‘FitnessCenter’

.. py:attribute:: FoodMarket
:value: ‘FoodMarket’

.. py:attribute:: Fortress
:value: ‘Fortress’

.. py:attribute:: GasStation
:value: ‘GasStation’

.. py:attribute:: GoKart
:value: ‘GoKart’

.. py:attribute:: Golf
:value: ‘Golf’

.. py:attribute:: Hiking
:value: ‘Hiking’

.. py:attribute:: Hospital
:value: ‘Hospital’

.. py:attribute:: Hotel
:value: ‘Hotel’

.. py:attribute:: Kayaking
:value: ‘Kayaking’

.. py:attribute:: Landmark
:value: ‘Landmark’

.. py:attribute:: Laundry
:value: ‘Laundry’

.. py:attribute:: Library
:value: ‘Library’

.. py:attribute:: Mailbox
:value: ‘Mailbox’

.. py:attribute:: Marina
:value: ‘Marina’

.. py:attribute:: MiniGolf
:value: ‘MiniGolf’

.. py:attribute:: MovieTheater
:value: ‘MovieTheater’

.. py:attribute:: Museum
:value: ‘Museum’

.. py:attribute:: MusicVenue
:value: ‘MusicVenue’

.. py:attribute:: NationalMonument
:value: ‘NationalMonument’

.. py:attribute:: NationalPark
:value: ‘NationalPark’

.. py:attribute:: Nightlife
:value: ‘Nightlife’

.. py:attribute:: Park
:value: ‘Park’

.. py:attribute:: Parking
:value: ‘Parking’

.. py:attribute:: Pharmacy
:value: ‘Pharmacy’

.. py:attribute:: Planetarium
:value: ‘Planetarium’

.. py:attribute:: Playground
:value: ‘Playground’

.. py:attribute:: Police
:value: ‘Police’

.. py:attribute:: PostOffice
:value: ‘PostOffice’

.. py:attribute:: PublicTransport
:value: ‘PublicTransport’

.. py:attribute:: ReligiousSite
:value: ‘ReligiousSite’

.. py:attribute:: Restaurant
:value: ‘Restaurant’

.. py:attribute:: Restroom
:value: ‘Restroom’

.. py:attribute:: RockClimbing
:value: ‘RockClimbing’

.. py:attribute:: RVPark
:value: ‘RVPark’

.. py:attribute:: School
:value: ‘School’

.. py:attribute:: SkatePark
:value: ‘SkatePark’

.. py:attribute:: Skating
:value: ‘Skating’

.. py:attribute:: Skiing
:value: ‘Skiing’

.. py:attribute:: Soccer
:value: ‘Soccer’

.. py:attribute:: Spa
:value: ‘Spa’

.. py:attribute:: Stadium
:value: ‘Stadium’

.. py:attribute:: Store
:value: ‘Store’

.. py:attribute:: Surfing
:value: ‘Surfing’

.. py:attribute:: Swimming
:value: ‘Swimming’

.. py:attribute:: Tennis
:value: ‘Tennis’

.. py:attribute:: Theater
:value: ‘Theater’

.. py:attribute:: University
:value: ‘University’

.. py:attribute:: Volleyball
:value: ‘Volleyball’

.. py:attribute:: Winery
:value: ‘Winery’

.. py:attribute:: Zoo
:value: ‘Zoo’

.. py:class:: SearchResultType

Bases: :py:obj:`enum.StrEnum`

Result type filter for /v1/search.

.. py:attribute:: poi
:value: ‘poi’

.. py:attribute:: address
:value: ‘address’

.. py:attribute:: physicalFeature
:value: ‘physicalFeature’

.. py:attribute:: pointOfInterest
:value: ‘pointOfInterest’

.. py:class:: SearchACResultType

Bases: :py:obj:`enum.StrEnum`

Result type filter for /v1/searchAutocomplete.

.. py:attribute:: poi
:value: ‘poi’

.. py:attribute:: address
:value: ‘address’

.. py:attribute:: physicalFeature
:value: ‘physicalFeature’

.. py:attribute:: pointOfInterest
:value: ‘pointOfInterest’

.. py:attribute:: query
:value: ‘query’

.. py:class:: SearchRegionPriority

Bases: :py:obj:`enum.StrEnum`

Importance of searchRegion for /v1/search and /v1/searchAutocomplete.

Apple possible values: default, required.

.. py:attribute:: default
:value: ‘default’

.. py:attribute:: required
:value: ‘required’

.. py:class:: Location(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

A coordinate pair from Apple Maps API.

latitude: north-south position (e.g. 37.334)
longitude: east-west position (e.g. -122.009)

.. py:attribute:: latitude
:type:  float

.. py:attribute:: longitude
:type:  float

.. py:class:: StructuredAddress(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Detailed address components of a place.

Apple uses different terminology than most geocoding APIs:

- locality = city
- administrativeArea = state/province name
- administrativeAreaCode = state/province short code (e.g. “NY”)
- subAdministrativeArea = county name
- postCode = postal/ZIP code
- fullThoroughfare = full street address (number + street, e.g. “841 Broadway”)
- thoroughfare = street name (e.g. “Broadway”)
- subThoroughfare = street/house number (e.g. “841”)
- subLocality = neighborhood or area within the city
- areasOfInterest = common names for the surrounding area
- dependentLocalities = neighborhood names

.. py:attribute:: administrativeArea
:type:  str | None
:value: None

.. py:attribute:: administrativeAreaCode
:type:  str | None
:value: None

.. py:attribute:: subAdministrativeArea
:type:  str | None
:value: None

.. py:attribute:: areasOfInterest
:type:  list[str] | None
:value: None

.. py:attribute:: dependentLocalities
:type:  list[str] | None
:value: None

.. py:attribute:: fullThoroughfare
:type:  str | None
:value: None

.. py:attribute:: locality
:type:  str | None
:value: None

.. py:attribute:: postCode
:type:  str | None
:value: None

.. py:attribute:: subLocality
:type:  str | None
:value: None

.. py:attribute:: subThoroughfare
:type:  str | None
:value: None

.. py:attribute:: thoroughfare
:type:  str | None
:value: None

.. py:class:: MapRegion(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

A rectangular bounding box on a map.

Expressed as south-west and north-east corners.

.. py:attribute:: eastLongitude
:type:  float

.. py:attribute:: northLatitude
:type:  float

.. py:attribute:: southLatitude
:type:  float

.. py:attribute:: westLongitude
:type:  float

.. py:class:: Place(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

A place returned by geocode, reverseGeocode, or place lookup endpoints.

coordinate: lat/lng of the place
formattedAddressLines: human-readable address lines (e.g. [“841 Broadway”, “New York, NY 10003”])
structuredAddress: parsed address components
displayMapRegion: suggested map viewport for displaying this place

.. py:attribute:: id
:type:  str | None
:value: None

.. py:attribute:: name
:type:  str | None
:value: None

.. py:attribute:: coordinate
:type:  Location | None
:value: None

.. py:attribute:: formattedAddressLines
:type:  list[str] | None
:value: None

.. py:attribute:: structuredAddress
:type:  StructuredAddress | None
:value: None

.. py:attribute:: country
:type:  str | None
:value: None

.. py:attribute:: countryCode
:type:  str | None
:value: None

.. py:attribute:: displayMapRegion
:type:  MapRegion | None
:value: None

.. py:attribute:: alternateIds
:type:  list[str] | None
:value: None

.. py:class:: SearchPlace(/, \*\*data: Any)

Bases: :py:obj:`Place`

Extended Place returned by /v1/search with POI category info.

poiCategory: point-of-interest category (e.g. Restaurant, MovieTheater).
Unknown values from Apple fail validation so we notice and add support.

.. py:attribute:: poiCategory
:type:  PoiCategory | None
:value: None

.. py:class:: PlaceResults(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Response from /v1/geocode and /v1/reverseGeocode.

results: list of Place objects matching the query

.. py:attribute:: results
:type:  list[Place]

.. py:class:: PaginationInfo(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Pagination metadata from /v1/search when enablePagination is true.

nextPageToken / prevPageToken: opaque tokens for pageToken on the next request
totalPageCount: total pages available
totalResults: total matching results

.. py:attribute:: nextPageToken
:type:  str | None
:value: None

.. py:attribute:: prevPageToken
:type:  str | None
:value: None

.. py:attribute:: totalPageCount
:type:  int | float | None
:value: None

.. py:attribute:: totalResults
:type:  int | float | None
:value: None

.. py:class:: SearchResponse(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Response from /v1/search.

results: list of SearchPlace objects with optional POI category
displayMapRegion: suggested map viewport encompassing all results
paginationInfo: present when the request set enablePagination

.. py:attribute:: results
:type:  list[SearchPlace]

.. py:attribute:: displayMapRegion
:type:  MapRegion | None
:value: None

.. py:attribute:: paginationInfo
:type:  PaginationInfo | None
:value: None

.. py:class:: AutocompleteResult(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

A single autocomplete suggestion from /v1/searchAutocomplete.

completionUrl: relative URL to /v1/search to fetch full details for this suggestion
displayLines: raw text lines Apple returns — use completionTitle / completionSubtitle instead
location: approximate coordinate of the suggestion
structuredAddress: parsed address components if available

.. py:attribute:: completionUrl
:type:  str | None
:value: None

.. py:attribute:: displayLines
:type:  list[str] | None
:value: None

.. py:attribute:: location
:type:  Location | None
:value: None

.. py:attribute:: structuredAddress
:type:  StructuredAddress | None
:value: None

.. py:property:: completionTitle
:type: str | None

```none
  Primary display text (e.g. place name or street address).
```

.. py:property:: completionSubtitle
:type: str | None

```none
  Secondary display text (e.g. city, state).
```

.. py:class:: SearchAutocompleteResponse(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Response from /v1/searchAutocomplete.

results: list of autocomplete suggestions

.. py:attribute:: results
:type:  list[AutocompleteResult]

.. py:class:: TokenResponse(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Response from /v1/token.

accessToken: short-lived Bearer token for API requests
expiresInSeconds: token lifetime (typically 1800 = 30 minutes)

.. py:attribute:: accessToken
:type:  str

.. py:attribute:: expiresInSeconds
:type:  int

.. py:class:: GeocodeResult(/, \*\*data: Any)

Bases: :py:obj:`pydantic.BaseModel`

Provider-agnostic geocode result.

Identical to radar-mapping-api’s GeocodeResult for drop-in replacement.
This abstraction allows swapping Apple Maps for Radar without changing consuming code.

.. py:attribute:: lat
:type:  float

.. py:attribute:: lon
:type:  float

.. py:attribute:: address1
:type:  str | None
:value: None

.. py:attribute:: address2
:type:  str | None
:value: None

.. py:attribute:: postal_code
:type:  str | None

.. py:attribute:: city
:type:  str | None

.. py:attribute:: state_code
:type:  str | None

.. py:attribute:: country_code
:type:  str | None
:value: None

.. py:attribute:: formatted_address
:type:  str | None
