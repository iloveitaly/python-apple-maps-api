# apple_maps_api.helpers

.. py:module:: apple_maps_api.helpers

.. autoapi-nested-parse::

Helper functions for common geocoding operations.

## Attributes

.. autoapisummary::

apple_maps_api.helpers.log

## Functions

.. autoapisummary::

apple_maps_api.helpers.geocode_postal_code
apple_maps_api.helpers.geocode_coordinates

## Module Contents

.. py:data:: log

.. py:function:: geocode_postal_code(client: apple_maps_api.client.AppleMapsClient, \*, postal_code: str, country: str = ‘US’) -> apple_maps_api.models.GeocodeResult | None

Geocode a postal code and extract coordinates and address information.

Args:
client: AppleMapsClient instance to use for geocoding
postal_code: The postal code to geocode
country: Country code (default: “US”)

Returns:
GeocodeResult with lat, lon, city, and state information.
Returns None if geocoding fails.

.. py:function:: geocode_coordinates(client: apple_maps_api.client.AppleMapsClient, \*, lat: float, lon: float) -> apple_maps_api.models.GeocodeResult | None

Reverse geocode coordinates and extract address information.

Args:
client: AppleMapsClient instance to use for geocoding
lat: Latitude
lon: Longitude

Returns:
GeocodeResult with lat, lon, zip_code, city, and state information.
Returns None if geocoding fails.
