# apple_maps_api.models

Pydantic models for Apple Maps Server API responses.

Model names and field names match Apple’s official API documentation exactly.
Docstrings explain what each field represents in familiar terms.

See: [https://developer.apple.com/documentation/applemapsserverapi](https://developer.apple.com/documentation/applemapsserverapi)

## Classes

| [`AddressCategory`](#apple_maps_api.models.AddressCategory)            | Enum where members are also (and must be) strings                       |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------|
| [`PoiCategory`](#apple_maps_api.models.PoiCategory)                | Enum where members are also (and must be) strings                       |
| [`SearchResultType`](#apple_maps_api.models.SearchResultType)           | Result type filter for /v1/search.                                      |
| [`SearchACResultType`](#apple_maps_api.models.SearchACResultType)         | Result type filter for /v1/searchAutocomplete.                          |
| [`SearchRegionPriority`](#apple_maps_api.models.SearchRegionPriority)       | Importance of searchRegion for /v1/search and /v1/searchAutocomplete.   |
| [`Location`](#apple_maps_api.models.Location)                   | A coordinate pair from Apple Maps API.                                  |
| [`StructuredAddress`](#apple_maps_api.models.StructuredAddress)          | Detailed address components of a place.                                 |
| [`MapRegion`](#apple_maps_api.models.MapRegion)                  | A rectangular bounding box on a map.                                    |
| [`Place`](#apple_maps_api.models.Place)                      | A place returned by geocode, reverseGeocode, or place lookup endpoints. |
| [`SearchPlace`](#apple_maps_api.models.SearchPlace)                | Extended Place returned by /v1/search with POI category info.           |
| [`PlaceResults`](#apple_maps_api.models.PlaceResults)               | Response from /v1/geocode and /v1/reverseGeocode.                       |
| [`PaginationInfo`](#apple_maps_api.models.PaginationInfo)             | Pagination metadata from /v1/search when enablePagination is true.      |
| [`SearchResponse`](#apple_maps_api.models.SearchResponse)             | Response from /v1/search.                                               |
| [`AutocompleteResult`](#apple_maps_api.models.AutocompleteResult)         | A single autocomplete suggestion from /v1/searchAutocomplete.           |
| [`SearchAutocompleteResponse`](#apple_maps_api.models.SearchAutocompleteResponse) | Response from /v1/searchAutocomplete.                                   |
| [`TokenResponse`](#apple_maps_api.models.TokenResponse)              | Response from /v1/token.                                                |
| [`GeocodeResult`](#apple_maps_api.models.GeocodeResult)              | Provider-agnostic geocode result.                                       |

## Module Contents

### *class* apple_maps_api.models.AddressCategory

Bases: [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)

Enum where members are also (and must be) strings

#### Country *= 'Country'*

#### AdministrativeArea *= 'AdministrativeArea'*

#### SubAdministrativeArea *= 'SubAdministrativeArea'*

#### Locality *= 'Locality'*

#### SubLocality *= 'SubLocality'*

#### PostalCode *= 'PostalCode'*

### *class* apple_maps_api.models.PoiCategory

Bases: [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)

Enum where members are also (and must be) strings

#### Airport *= 'Airport'*

#### AirportGate *= 'AirportGate'*

#### AirportTerminal *= 'AirportTerminal'*

#### AmusementPark *= 'AmusementPark'*

#### AnimalService *= 'AnimalService'*

#### Aquarium *= 'Aquarium'*

#### ATM *= 'ATM'*

#### AutomotiveRepair *= 'AutomotiveRepair'*

#### Bakery *= 'Bakery'*

#### Bank *= 'Bank'*

#### Baseball *= 'Baseball'*

#### Basketball *= 'Basketball'*

#### Beach *= 'Beach'*

#### Beauty *= 'Beauty'*

#### Bowling *= 'Bowling'*

#### Brewery *= 'Brewery'*

#### Cafe *= 'Cafe'*

#### Campground *= 'Campground'*

#### CarRental *= 'CarRental'*

#### Castle *= 'Castle'*

#### ConventionCenter *= 'ConventionCenter'*

#### Distillery *= 'Distillery'*

#### EVCharger *= 'EVCharger'*

#### Fairground *= 'Fairground'*

#### FireStation *= 'FireStation'*

#### Fishing *= 'Fishing'*

#### FitnessCenter *= 'FitnessCenter'*

#### FoodMarket *= 'FoodMarket'*

#### Fortress *= 'Fortress'*

#### GasStation *= 'GasStation'*

#### GoKart *= 'GoKart'*

#### Golf *= 'Golf'*

#### Hiking *= 'Hiking'*

#### Hospital *= 'Hospital'*

#### Hotel *= 'Hotel'*

#### Kayaking *= 'Kayaking'*

#### Landmark *= 'Landmark'*

#### Laundry *= 'Laundry'*

#### Library *= 'Library'*

#### Mailbox *= 'Mailbox'*

#### Marina *= 'Marina'*

#### MiniGolf *= 'MiniGolf'*

#### MovieTheater *= 'MovieTheater'*

#### Museum *= 'Museum'*

#### MusicVenue *= 'MusicVenue'*

#### NationalMonument *= 'NationalMonument'*

#### NationalPark *= 'NationalPark'*

#### Nightlife *= 'Nightlife'*

#### Park *= 'Park'*

#### Parking *= 'Parking'*

#### Pharmacy *= 'Pharmacy'*

#### Planetarium *= 'Planetarium'*

#### Playground *= 'Playground'*

#### Police *= 'Police'*

#### PostOffice *= 'PostOffice'*

#### PublicTransport *= 'PublicTransport'*

#### ReligiousSite *= 'ReligiousSite'*

#### Restaurant *= 'Restaurant'*

#### Restroom *= 'Restroom'*

#### RockClimbing *= 'RockClimbing'*

#### RVPark *= 'RVPark'*

#### School *= 'School'*

#### SkatePark *= 'SkatePark'*

#### Skating *= 'Skating'*

#### Skiing *= 'Skiing'*

#### Soccer *= 'Soccer'*

#### Spa *= 'Spa'*

#### Stadium *= 'Stadium'*

#### Store *= 'Store'*

#### Surfing *= 'Surfing'*

#### Swimming *= 'Swimming'*

#### Tennis *= 'Tennis'*

#### Theater *= 'Theater'*

#### University *= 'University'*

#### Volleyball *= 'Volleyball'*

#### Winery *= 'Winery'*

#### Zoo *= 'Zoo'*

### *class* apple_maps_api.models.SearchResultType

Bases: [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)

Result type filter for /v1/search.

#### poi *= 'poi'*

#### address *= 'address'*

#### physicalFeature *= 'physicalFeature'*

#### pointOfInterest *= 'pointOfInterest'*

### *class* apple_maps_api.models.SearchACResultType

Bases: [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)

Result type filter for /v1/searchAutocomplete.

#### poi *= 'poi'*

#### address *= 'address'*

#### physicalFeature *= 'physicalFeature'*

#### pointOfInterest *= 'pointOfInterest'*

#### query *= 'query'*

### *class* apple_maps_api.models.SearchRegionPriority

Bases: [`enum.StrEnum`](https://docs.python.org/3/library/enum.html#enum.StrEnum)

Importance of searchRegion for /v1/search and /v1/searchAutocomplete.

Apple possible values: default, required.

#### default *= 'default'*

#### required *= 'required'*

### *class* apple_maps_api.models.Location(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

A coordinate pair from Apple Maps API.

latitude: north-south position (e.g. 37.334)
longitude: east-west position (e.g. -122.009)

#### latitude *: [float](https://docs.python.org/3/library/functions.html#float)*

#### longitude *: [float](https://docs.python.org/3/library/functions.html#float)*

### *class* apple_maps_api.models.StructuredAddress(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

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

#### administrativeArea *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### administrativeAreaCode *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### subAdministrativeArea *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### areasOfInterest *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### dependentLocalities *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### fullThoroughfare *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### locality *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### postCode *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### subLocality *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### subThoroughfare *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### thoroughfare *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

### *class* apple_maps_api.models.MapRegion(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

A rectangular bounding box on a map.

Expressed as south-west and north-east corners.

#### eastLongitude *: [float](https://docs.python.org/3/library/functions.html#float)*

#### northLatitude *: [float](https://docs.python.org/3/library/functions.html#float)*

#### southLatitude *: [float](https://docs.python.org/3/library/functions.html#float)*

#### westLongitude *: [float](https://docs.python.org/3/library/functions.html#float)*

### *class* apple_maps_api.models.Place(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

A place returned by geocode, reverseGeocode, or place lookup endpoints.

coordinate: lat/lng of the place
formattedAddressLines: human-readable address lines (e.g. [“841 Broadway”, “New York, NY 10003”])
structuredAddress: parsed address components
displayMapRegion: suggested map viewport for displaying this place

#### id *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### name *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### coordinate *: [Location](#apple_maps_api.models.Location) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### formattedAddressLines *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### structuredAddress *: [StructuredAddress](#apple_maps_api.models.StructuredAddress) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### country *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### countryCode *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### displayMapRegion *: [MapRegion](#apple_maps_api.models.MapRegion) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### alternateIds *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

### *class* apple_maps_api.models.SearchPlace(/, \*\*data: Any)

Bases: [`Place`](#apple_maps_api.models.Place)

Extended Place returned by /v1/search with POI category info.

poiCategory: point-of-interest category (e.g. Restaurant, MovieTheater).
Unknown values from Apple fail validation so we notice and add support.

#### poiCategory *: [PoiCategory](#apple_maps_api.models.PoiCategory) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

### *class* apple_maps_api.models.PlaceResults(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Response from /v1/geocode and /v1/reverseGeocode.

results: list of Place objects matching the query

#### results *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[Place](#apple_maps_api.models.Place)]*

### *class* apple_maps_api.models.PaginationInfo(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Pagination metadata from /v1/search when enablePagination is true.

nextPageToken / prevPageToken: opaque tokens for pageToken on the next request
totalPageCount: total pages available
totalResults: total matching results

#### nextPageToken *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### prevPageToken *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### totalPageCount *: [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### totalResults *: [int](https://docs.python.org/3/library/functions.html#int) | [float](https://docs.python.org/3/library/functions.html#float) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

### *class* apple_maps_api.models.SearchResponse(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Response from /v1/search.

results: list of SearchPlace objects with optional POI category
displayMapRegion: suggested map viewport encompassing all results
paginationInfo: present when the request set enablePagination

#### results *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[SearchPlace](#apple_maps_api.models.SearchPlace)]*

#### displayMapRegion *: [MapRegion](#apple_maps_api.models.MapRegion) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### paginationInfo *: [PaginationInfo](#apple_maps_api.models.PaginationInfo) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

### *class* apple_maps_api.models.AutocompleteResult(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

A single autocomplete suggestion from /v1/searchAutocomplete.

completionUrl: relative URL to /v1/search to fetch full details for this suggestion
displayLines: raw text lines Apple returns — use completionTitle / completionSubtitle instead
location: approximate coordinate of the suggestion
structuredAddress: parsed address components if available

#### completionUrl *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### displayLines *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[str](https://docs.python.org/3/library/stdtypes.html#str)] | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### location *: [Location](#apple_maps_api.models.Location) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### structuredAddress *: [StructuredAddress](#apple_maps_api.models.StructuredAddress) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### *property* completionTitle *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

Primary display text (e.g. place name or street address).

#### *property* completionSubtitle *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

Secondary display text (e.g. city, state).

### *class* apple_maps_api.models.SearchAutocompleteResponse(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Response from /v1/searchAutocomplete.

results: list of autocomplete suggestions

#### results *: [list](https://docs.python.org/3/library/stdtypes.html#list)[[AutocompleteResult](#apple_maps_api.models.AutocompleteResult)]*

### *class* apple_maps_api.models.TokenResponse(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Response from /v1/token.

accessToken: short-lived Bearer token for API requests
expiresInSeconds: token lifetime (typically 1800 = 30 minutes)

#### accessToken *: [str](https://docs.python.org/3/library/stdtypes.html#str)*

#### expiresInSeconds *: [int](https://docs.python.org/3/library/functions.html#int)*

### *class* apple_maps_api.models.GeocodeResult(/, \*\*data: Any)

Bases: [`pydantic.BaseModel`](https://docs.pydantic.dev/latest/api/pydantic/base_model/#pydantic.BaseModel)

Provider-agnostic geocode result.

Identical to radar-mapping-api’s GeocodeResult for drop-in replacement.
This abstraction allows swapping Apple Maps for Radar without changing consuming code.

#### lat *: [float](https://docs.python.org/3/library/functions.html#float)*

#### lon *: [float](https://docs.python.org/3/library/functions.html#float)*

#### address1 *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### address2 *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### postal_code *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### city *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### state_code *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*

#### country_code *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)* *= None*

#### formatted_address *: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None)*
