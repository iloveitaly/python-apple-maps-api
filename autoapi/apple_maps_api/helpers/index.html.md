# apple_maps_api.helpers

Helper functions for common geocoding operations.

## Attributes

| [`log`](#apple_maps_api.helpers.log)   |    |
|----------------------------------------|----|

## Functions

| [`geocode_postal_code`](#apple_maps_api.helpers.geocode_postal_code)(...)   | Geocode a postal code and extract coordinates and address information.   |
|-----------------------------------------------------------------------------|--------------------------------------------------------------------------|
| [`geocode_coordinates`](#apple_maps_api.helpers.geocode_coordinates)(...)   | Reverse geocode coordinates and extract address information.             |

## Module Contents

### apple_maps_api.helpers.log

### apple_maps_api.helpers.geocode_postal_code(client: [apple_maps_api.client.AppleMapsClient](../client/index.md#apple_maps_api.client.AppleMapsClient), , postal_code: [str](https://docs.python.org/3/library/stdtypes.html#str), country: [str](https://docs.python.org/3/library/stdtypes.html#str) = 'US') → [apple_maps_api.models.GeocodeResult](../models/index.md#apple_maps_api.models.GeocodeResult) | [None](https://docs.python.org/3/library/constants.html#None)

Geocode a postal code and extract coordinates and address information.

Args:
: client: AppleMapsClient instance to use for geocoding
  postal_code: The postal code to geocode
  country: Country code (default: “US”)

Returns:
: GeocodeResult with lat, lon, city, and state information.
  Returns None if geocoding fails.

### apple_maps_api.helpers.geocode_coordinates(client: [apple_maps_api.client.AppleMapsClient](../client/index.md#apple_maps_api.client.AppleMapsClient), , lat: [float](https://docs.python.org/3/library/functions.html#float), lon: [float](https://docs.python.org/3/library/functions.html#float)) → [apple_maps_api.models.GeocodeResult](../models/index.md#apple_maps_api.models.GeocodeResult) | [None](https://docs.python.org/3/library/constants.html#None)

Reverse geocode coordinates and extract address information.

Args:
: client: AppleMapsClient instance to use for geocoding
  lat: Latitude
  lon: Longitude

Returns:
: GeocodeResult with lat, lon, zip_code, city, and state information.
  Returns None if geocoding fails.
