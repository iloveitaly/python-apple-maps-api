# apple_maps_api.client

Apple Maps Server API client library.

API docs: [https://developer.apple.com/documentation/applemapsserverapi](https://developer.apple.com/documentation/applemapsserverapi)

This library provides a Python client for the Apple Maps Server API with JWT-based
authentication, automatic token management, and retry logic.

## Attributes

| [`log`](#apple_maps_api.client.log)   |    |
|---------------------------------------|----|

## Classes

| [`GeocodeOptionsLatLng`](#apple_maps_api.client.GeocodeOptionsLatLng)           | Geocode options with required `lat` and `lng` location bias.                                                     |
|---------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [`GeocodeOptions`](#apple_maps_api.client.GeocodeOptions)                       | All optional kwargs for [`AppleMapsClient.geocode()`](#apple_maps_api.client.AppleMapsClient.geocode).           |
| [`SearchOptionsLatLng`](#apple_maps_api.client.SearchOptionsLatLng)             | Search options with required `lat` and `lng` location bias.                                                      |
| [`SearchOptions`](#apple_maps_api.client.SearchOptions)                         | All optional kwargs for [`AppleMapsClient.search()`](#apple_maps_api.client.AppleMapsClient.search).             |
| [`AutocompleteOptionsLatLng`](#apple_maps_api.client.AutocompleteOptionsLatLng) | Autocomplete options with required `lat` and `lng` location bias.                                                |
| [`AutocompleteOptions`](#apple_maps_api.client.AutocompleteOptions)             | All optional kwargs for [`AppleMapsClient.autocomplete()`](#apple_maps_api.client.AppleMapsClient.autocomplete). |
| [`AppleMapsClient`](#apple_maps_api.client.AppleMapsClient)                     | A client for the Apple Maps Server API.                                                                          |

## Module Contents

### apple_maps_api.client.log

### *class* apple_maps_api.client.GeocodeOptionsLatLng

Bases: `_GeocodeOptionsBase`

Geocode options with required `lat` and `lng` location bias.

#### lat *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

#### lng *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

### *class* apple_maps_api.client.GeocodeOptions

Bases: `_GeocodeOptionsBase`

All optional kwargs for [`AppleMapsClient.geocode()`](#apple_maps_api.client.AppleMapsClient.geocode).

#### lat *: [float](https://docs.python.org/3/library/functions.html#float)*

#### lng *: [float](https://docs.python.org/3/library/functions.html#float)*

### *class* apple_maps_api.client.SearchOptionsLatLng

Bases: `_SearchOptionsBase`

Search options with required `lat` and `lng` location bias.

#### lat *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

#### lng *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

### *class* apple_maps_api.client.SearchOptions

Bases: `_SearchOptionsBase`

All optional kwargs for [`AppleMapsClient.search()`](#apple_maps_api.client.AppleMapsClient.search).

#### lat *: [float](https://docs.python.org/3/library/functions.html#float)*

#### lng *: [float](https://docs.python.org/3/library/functions.html#float)*

### *class* apple_maps_api.client.AutocompleteOptionsLatLng

Bases: `_AutocompleteOptionsBase`

Autocomplete options with required `lat` and `lng` location bias.

#### lat *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

#### lng *: Required[[float](https://docs.python.org/3/library/functions.html#float)]*

### *class* apple_maps_api.client.AutocompleteOptions

Bases: `_AutocompleteOptionsBase`

All optional kwargs for [`AppleMapsClient.autocomplete()`](#apple_maps_api.client.AppleMapsClient.autocomplete).

#### lat *: [float](https://docs.python.org/3/library/functions.html#float)*

#### lng *: [float](https://docs.python.org/3/library/functions.html#float)*

### *class* apple_maps_api.client.AppleMapsClient(, team_id: [str](https://docs.python.org/3/library/stdtypes.html#str), key_id: [str](https://docs.python.org/3/library/stdtypes.html#str), private_key: [str](https://docs.python.org/3/library/stdtypes.html#str), origin: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None)

A client for the Apple Maps Server API.

Handles JWT-based authentication with automatic token refresh,
and provides methods for geocoding, reverse geocoding, search, and autocomplete.

#### team_id

#### key_id

#### origin *= None*

#### private_key

#### base_url *= 'https://maps-api.apple.com'*

#### *classmethod* from_env() → [AppleMapsClient](#apple_maps_api.client.AppleMapsClient)

Construct a client from APPLE_MAPS_\* environment variables.

Required:
- APPLE_MAPS_TEAM_ID
- APPLE_MAPS_KEY_ID
- APPLE_MAPS_P8_KEY

Optional:
- APPLE_MAPS_ORIGIN

#### create_token() → [str](https://docs.python.org/3/library/stdtypes.html#str)

Return a valid Maps access token for Apple Maps Server API use.

This is the *access token* (not the auth JWT) suitable for server-side
API calls (geocode, search, etc.). It is NOT suitable for MapKit JS.
Use create_mapkit_token() for browser-side MapKit JS initialization.

Spec: [https://developer.apple.com/documentation/applemapsserverapi/-v1-token](https://developer.apple.com/documentation/applemapsserverapi/-v1-token)

#### create_mapkit_token(, ttl_seconds: [int](https://docs.python.org/3/library/functions.html#int) = \_DEFAULT_JWT_TTL_SECONDS) → [str](https://docs.python.org/3/library/stdtypes.html#str)

Return a signed JWT for MapKit JS browser initialization.

MapKit JS requires the raw signed JWT, not the Server API access token.
Pass this to the authorizationCallback done() function.
If origin was set on the client, the token is restricted to that domain.

* **Parameters:**
  **ttl_seconds** – JWT lifetime in seconds (default: 1 hour).
  Apple does not document a maximum for Maps tokens.

Spec:
[https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)
[https://developer.apple.com/documentation/mapkitjs/creating-and-using-tokens-with-mapkit-js](https://developer.apple.com/documentation/mapkitjs/creating-and-using-tokens-with-mapkit-js)

#### geocode(query: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*kwargs: Unpack[[GeocodeOptionsLatLng](#apple_maps_api.client.GeocodeOptionsLatLng)]) → [apple_maps_api.models.PlaceResults](../models/index.md#apple_maps_api.models.PlaceResults)

#### geocode(query: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*kwargs: Unpack[\_GeocodeOptionsBase]) → [apple_maps_api.models.PlaceResults](../models/index.md#apple_maps_api.models.PlaceResults)

Convert an address string to coordinates.

Maps to GET /v1/geocode.

* **Parameters:**
  * **query** – Address to geocode (e.g., “1 Apple Park Way”).
  * **limit_to_countries** – ISO 3166-1 alpha-2 country codes to limit results
    (e.g. `["US", "CA"]`).
  * **lang** – BCP 47 language code (default: “en-US”).
  * **lat** – Latitude for app-defined search bias (must pass with lng).
    Sent as Apple’s `searchLocation`.
  * **lng** – Longitude for app-defined search bias (must pass with lat).
  * **search_region** – App-defined bounding-box hint as `MapRegion`.
  * **user_lat** – Latitude of the user’s position (must pass with user_lng).
    Used for ranking/relevance; if `lat`/`lng` are omitted, some
    endpoints may fall back to this as the search hint.
  * **user_lng** – Longitude of the user’s position (must pass with user_lat).

#### reverse_geocode(, lat: [float](https://docs.python.org/3/library/functions.html#float), lng: [float](https://docs.python.org/3/library/functions.html#float), lang: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [apple_maps_api.models.PlaceResults](../models/index.md#apple_maps_api.models.PlaceResults)

Convert coordinates to an address.

Maps to GET /v1/reverseGeocode.

* **Parameters:**
  * **lat** – Latitude of the point to reverse geocode.
  * **lng** – Longitude of the point to reverse geocode.
  * **lang** – BCP 47 language code (default: “en-US”).

#### search(query: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*kwargs: Unpack[[SearchOptionsLatLng](#apple_maps_api.client.SearchOptionsLatLng)]) → [apple_maps_api.models.SearchResponse](../models/index.md#apple_maps_api.models.SearchResponse)

#### search(query: [str](https://docs.python.org/3/library/stdtypes.html#str) = '', \*\*kwargs: Unpack[\_SearchOptionsBase]) → [apple_maps_api.models.SearchResponse](../models/index.md#apple_maps_api.models.SearchResponse)

Search for places by name or category.

Maps to GET /v1/search.

Location bias (optional): pass `lat=` and `lng=` together.

For page 2+, pass only `page_token` from a prior response’s
`paginationInfo.nextPageToken`. Apple rejects other search params
(including `q` and `enablePagination`) on token requests.

* **Parameters:**
  * **query** – Search query (e.g., “coffee”, “Apple Park”). Required
    unless `page_token` is set.
  * **lat** – Latitude for app-defined search bias (must pass with lng).
    Sent as Apple’s `searchLocation` — “search near this map point”.
  * **lng** – Longitude for app-defined search bias (must pass with lat).
  * **categories** – POI categories to include (e.g. `["MovieTheater", "Cafe"]`).
  * **exclude_categories** – POI categories to exclude (e.g. `["Parking"]`).
  * **limit_to_countries** – ISO 3166-1 alpha-2 country codes
    (e.g. `["US", "CA"]`).
  * **lang** – BCP 47 language code (default: “en-US”).
  * **result_type_filter** – Result types (e.g. `["Poi", "Address"]`).
  * **search_region** – App-defined bounding-box hint as `MapRegion`.
  * **user_lat** – Latitude of the user’s position (must pass with user_lng).
    Used for ranking/relevance; Search may fall back to it as
    `searchLocation` when `lat`/`lng` are omitted.
  * **user_lng** – Longitude of the user’s position (must pass with user_lat).
  * **search_region_priority** – Importance of `search_region`
    (`SearchRegionPriority` or `"default"` / `"required"`).
  * **enable_pagination** – Request paginated results (first page only).
  * **page_token** – Token from `paginationInfo` for a subsequent page.
    When set, sent alone — do not combine with query or other filters.
  * **include_address_categories** – Address categories to include
    (e.g. `["AdministrativeArea"]`).
  * **exclude_address_categories** – Address categories to exclude.

#### autocomplete(query: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*kwargs: Unpack[[AutocompleteOptionsLatLng](#apple_maps_api.client.AutocompleteOptionsLatLng)]) → [apple_maps_api.models.SearchAutocompleteResponse](../models/index.md#apple_maps_api.models.SearchAutocompleteResponse)

#### autocomplete(query: [str](https://docs.python.org/3/library/stdtypes.html#str), \*\*kwargs: Unpack[\_AutocompleteOptionsBase]) → [apple_maps_api.models.SearchAutocompleteResponse](../models/index.md#apple_maps_api.models.SearchAutocompleteResponse)

Autocomplete partial addresses and place names.

Maps to GET /v1/searchAutocomplete.

Location bias (optional): pass `lat=` and `lng=` together.

Result count is fixed by Apple; the API has no limit/maxResults parameter.
For more results, use search() (supports enable_pagination) or
search_completion() to expand a single autocomplete hit.

* **Parameters:**
  * **query** – Partial address or place name to autocomplete.
  * **lat** – Latitude for app-defined search bias (must pass with lng).
    Sent as Apple’s `searchLocation` — “search near this map point”.
  * **lng** – Longitude for app-defined search bias (must pass with lat).
  * **limit_to_countries** – ISO 3166-1 alpha-2 country codes
    (e.g. `["US", "CA"]`).
  * **lang** – BCP 47 language code (default: “en-US”).
  * **result_type_filter** – Result types (e.g. `["Address", "Poi"]`).
  * **include_poi_categories** – POI categories to include
    (e.g. `["Cafe"]`).
  * **exclude_poi_categories** – POI categories to exclude.
  * **search_region** – App-defined bounding-box hint as `MapRegion`.
  * **user_lat** – Latitude of the user’s position (must pass with user_lng).
    Used for ranking/relevance; may fall back as `searchLocation`
    when `lat`/`lng` are omitted.
  * **user_lng** – Longitude of the user’s position (must pass with user_lat).
  * **search_region_priority** – Importance of `search_region`
    (`SearchRegionPriority` or `"default"` / `"required"`).
  * **include_address_categories** – Address categories to include.
  * **exclude_address_categories** – Address categories to exclude.

#### search_completion(completion: [apple_maps_api.models.AutocompleteResult](../models/index.md#apple_maps_api.models.AutocompleteResult) | [str](https://docs.python.org/3/library/stdtypes.html#str), , lang: [str](https://docs.python.org/3/library/stdtypes.html#str) | [None](https://docs.python.org/3/library/constants.html#None) = None) → [apple_maps_api.models.SearchResponse](../models/index.md#apple_maps_api.models.SearchResponse)

Resolve an autocomplete suggestion to full search results.

Maps to GET /v1/search using the completionUrl from an AutocompleteResult.
The completionUrl already encodes the query and opaque metadata Apple needs
to return precise results for the suggestion.

* **Parameters:**
  * **completion** – An AutocompleteResult or its completionUrl string.
  * **lang** – BCP 47 language code (e.g., “en-US”). Apple does not carry the
    language through the completionUrl, so callers must re-specify it here.
* **Raises:**
  [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError) – If the completion has no completionUrl.
