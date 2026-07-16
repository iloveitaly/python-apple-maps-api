[![Release Notes](https://img.shields.io/github/release/iloveitaly/apple-maps-api)](https://github.com/iloveitaly/apple-maps-api/releases)
[![Downloads](https://static.pepy.tech/badge/apple-maps-api/month)](https://pepy.tech/project/apple-maps-api)
![GitHub CI Status](https://github.com/iloveitaly/apple-maps-api/actions/workflows/build_and_publish.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Python Client for Apple Maps Server API

A modern, type-safe Python client for the [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi).

There's no python library for the Apple Maps API. Maps is super cheap compared to all of the alternatives, so with AI I figured it wouldn't be too hard to build a client library.

The goal of this library is to provide similar functionality to the radar python client.

## Installation

```bash
uv add apple-maps-api
```

For optional Sentry integration:

```bash
uv add apple-maps-api[sentry]
```

## Usage

### Basic Setup

You'll need your Team ID, Key ID, and the private key from your Apple Developer account.

```python
from apple_maps_api import AppleMapsClient

client = AppleMapsClient(
    team_id="YOUR_TEAM_ID",
    key_id="YOUR_KEY_ID",
    private_key="""-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----"""
)
```

Or load credentials from environment variables:

```bash
export APPLE_MAPS_TEAM_ID=...
export APPLE_MAPS_KEY_ID=...
export APPLE_MAPS_P8_KEY=...   # PEM or raw base64 DER
# optional: export APPLE_MAPS_ORIGIN=https://example.com
```

```python
from apple_maps_api import AppleMapsClient

client = AppleMapsClient.from_env()
```


### Geocoding

Convert an address string to coordinates:

```python
results = client.geocode("1 Apple Park Way, Cupertino, CA")

for place in results.results:
    print(f"{place.name}: {place.coordinate.latitude}, {place.coordinate.longitude}")

# place.name                              => "1 Apple Park Way"
# place.coordinate.latitude               => 37.334859
# place.coordinate.longitude              => -122.0090403
# place.formattedAddressLines             => ["1 Apple Park Way", "Cupertino, CA  95014", "United States"]
# place.structuredAddress.locality        => "Cupertino"
```

### Reverse Geocoding

Convert coordinates back to a structured address:

```python
results = client.reverse_geocode((37.3346, -122.0090))

if results.results:
    print(results.results[0].formattedAddressLines)

# place.formattedAddressLines      => ["Apple Park", "1 Apple Park Way", "Cupertino, CA  95014", "United States"]
# place.structuredAddress.locality => "Cupertino"
# place.structuredAddress.postCode => "95014"
```

### Place Search

Search for points of interest near a location:

```python
results = client.search("pizza", near="37.3346,-122.0090")

for place in results.results:
    print(f"{place.name} - {place.formattedAddressLines}")

# results.results[0].name                  => "Pizza My Heart"
# results.results[0].formattedAddressLines => ["19409 Stevens Creek Blvd", "Cupertino, CA  95014", "United States"]
# results.results[1].name                  => "Mountain Mike's Pizza"
# results.results[2].name                  => "Pizz'a Chicago"
```

### Address Autocomplete

Provide search completions for a partial query and filter by country:

```python
results = client.autocomplete("1 Apple Park", country_code="US")

for completion in results.results:
    print(completion.displayLines)

# results.results[0].displayLines => ["1 Apple Park Way", "Cupertino, CA, United States"]
# results.results[1].displayLines => ["1 Apple Hill Dr", "Natick, MA, United States"]
# results.results[0].completionUrl => "/v1/search?q=1%20Apple%20Park%20Way..."
```

### Helper Functions

The library includes high-level helpers for common geocoding operations:

```python
from apple_maps_api import geocode_postal_code, geocode_coordinates

# Geocode a postal code
result = geocode_postal_code(client, postal_code="95014", country="US")
# result.lat              => 37.2895111
# result.lon              => -122.0811912
# result.city             => "Cupertino"
# result.state_code       => "CA"
# result.postal_code      => "95014"
# result.formatted_address => "Cupertino, CA  95014, United States"

# Reverse geocode coordinates
result = geocode_coordinates(client, lat=37.3346, lon=-122.0090)
# result.address1          => "1 Apple Park Way"
# result.postal_code       => "95014"
# result.city              => "Cupertino"
# result.state_code        => "CA"
# result.formatted_address => "Apple Park, 1 Apple Park Way, Cupertino, CA  95014, United States"
```

## Example Payloads

These examples show the real data shapes returned by the Apple Maps API for common operations.

> **Note on city names:** Apple Maps uses its own administrative boundaries. The `city` field on `GeocodeResult` maps to `structuredAddress.locality`, which may differ from the colloquial city name. For example, postal code `90210` returns `city="Los Angeles"` even though the formatted address reads `"Beverly Hills"` — Beverly Hills is an independent city but Apple Maps assigns it to the LA locality.

### Geocoding a postal code

```python
result = geocode_postal_code(client, postal_code="10001")
# result.lat             => 40.7504876
# result.lon             => -74.0025705
# result.city            => "New York"
# result.state_code      => "NY"
# result.postal_code     => "10001"
# result.formatted_address => "New York, NY  10001, United States"
```

```python
result = geocode_postal_code(client, postal_code="90210")
# result.lat             => 34.1025226
# result.lon             => -118.4167959
# result.city            => "Los Angeles"   # NOT "Beverly Hills"
# result.state_code      => "CA"
# result.postal_code     => "90210"
# result.formatted_address => "Beverly Hills, CA  90210, United States"
```

### Reverse geocoding coordinates

```python
# Times Square, NYC
result = geocode_coordinates(client, lat=40.7589, lon=-73.9851)
# result.address1          => "1552–1568 Broadway"
# result.postal_code       => "10036"
# result.city              => "New York"
# result.state_code        => "NY"
# result.formatted_address => "Times Square, 1552–1568 Broadway, New York, NY  10036, United States"
```

### Raw `reverse_geocode` response — full `structuredAddress`

Apple Park, Cupertino CA (`37.3346, -122.0090`):

```python
place = client.reverse_geocode((37.3346, -122.0090)).results[0]
# place.name                                      => "Apple Park"
# place.formattedAddressLines                     => ["Apple Park", "1 Apple Park Way", "Cupertino, CA  95014", "United States"]
# place.structuredAddress.administrativeArea      => "California"
# place.structuredAddress.administrativeAreaCode  => "CA"
# place.structuredAddress.subAdministrativeArea   => None
# place.structuredAddress.locality                => "Cupertino"
# place.structuredAddress.subLocality             => None
# place.structuredAddress.fullThoroughfare        => "1 Apple Park Way"
# place.structuredAddress.thoroughfare            => "Apple Park Way"
# place.structuredAddress.subThoroughfare         => "1"
# place.structuredAddress.postCode                => "95014"
# place.structuredAddress.areasOfInterest         => ["Apple Park"]
# place.structuredAddress.dependentLocalities     => None
```

Times Square, NYC (`40.7589, -73.9851`):

```python
place = client.reverse_geocode((40.7589, -73.9851)).results[0]
# place.name                                      => "Times Square"
# place.formattedAddressLines                     => ["Times Square", "1552–1568 Broadway", "New York, NY  10036", "United States"]
# place.structuredAddress.administrativeArea      => "New York"
# place.structuredAddress.administrativeAreaCode  => "NY"
# place.structuredAddress.subAdministrativeArea   => None
# place.structuredAddress.locality                => "New York"
# place.structuredAddress.subLocality             => "Manhattan"
# place.structuredAddress.fullThoroughfare        => "1552–1568 Broadway"
# place.structuredAddress.thoroughfare            => "Broadway"
# place.structuredAddress.subThoroughfare         => "1552–1568"
# place.structuredAddress.postCode                => "10036"
# place.structuredAddress.areasOfInterest         => ["Times Square", "Manhattan"]
# place.structuredAddress.dependentLocalities     => ["Broadway", "Times Square", "Theater District", "Midtown Manhattan", "Midtown", "North Hudson"]
```

Beverly Hills, CA (`34.1025226, -118.4167959`) — note `locality` vs formatted address mismatch:

```python
place = client.reverse_geocode((34.1025226, -118.4167959)).results[0]
# place.name                                      => "1731 N Franklin Canyon Dr"
# place.formattedAddressLines                     => ["1731 N Franklin Canyon Dr", "Beverly Hills, CA  90210", "United States"]
# place.structuredAddress.administrativeArea      => "California"
# place.structuredAddress.administrativeAreaCode  => "CA"
# place.structuredAddress.subAdministrativeArea   => None
# place.structuredAddress.locality                => "Los Angeles"   # NOT "Beverly Hills"
# place.structuredAddress.subLocality             => "Beverly Crest"
# place.structuredAddress.fullThoroughfare        => "1731 N Franklin Canyon Dr"
# place.structuredAddress.thoroughfare            => "N Franklin Canyon Dr"
# place.structuredAddress.subThoroughfare         => "1731"
# place.structuredAddress.postCode                => "90210"
# place.structuredAddress.areasOfInterest         => None
# place.structuredAddress.dependentLocalities     => ["Beverly Crest"]
```

## API Reference

### AppleMapsClient

#### Construction

- `AppleMapsClient(team_id=..., key_id=..., private_key=..., origin=None)` - Construct with explicit credentials
- `AppleMapsClient.from_env()` - Construct from environment variables:
  - `APPLE_MAPS_TEAM_ID` (required)
  - `APPLE_MAPS_KEY_ID` (required)
  - `APPLE_MAPS_P8_KEY` (required; PEM or raw base64 DER)
  - `APPLE_MAPS_ORIGIN` (optional; MapKit JS domain restriction)

Raises `ValueError` if any required variable is missing or empty.

#### Methods

- `geocode(query, **options)` - Convert address to coordinates
- `reverse_geocode(coordinates, **options)` - Convert coordinates to address
- `search(query, **options)` - Search for places and POIs
- `autocomplete(query, **options)` - Provide search completions
- `create_token()` - Fetch a short-lived Apple Maps Server API access token
- `create_mapkit_token()` - Create a JWT for browser-side MapKit JS

### Models

All responses are returned as Pydantic models for easy integration and validation:

- `PlaceResults` - Response for geocoding and reverse geocoding
- `SearchResponse` - Response for search requests
- `SearchAutocompleteResponse` - Response for autocomplete requests
- `GeocodeResult` - A simplified, flattened representation of a geocoded location
- `Place` - Detailed information about a specific location or POI
- `Address` - Structured address data (street, city, state, etc.)

## Features

- **Automatic JWT Management**: Handles signing and periodic refresh of Apple's ES256 tokens.
- **Type-Safe**: Built with Pydantic models for all API responses, giving you excellent IDE support.
- **Resilient**: Automatic retries with exponential backoff for transient network and server errors.
- **Modern**: Uses `httpx` for synchronous requests, with a structure that's ready for future async support.

## [MIT License](LICENSE.md)

---

*This project was created from [iloveitaly/python-package-template](https://github.com/iloveitaly/python-package-template)*
