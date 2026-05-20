[![Release Notes](https://img.shields.io/github/release/iloveitaly/apple-maps-api)](https://github.com/iloveitaly/apple-maps-api/releases)
[![Downloads](https://static.pepy.tech/badge/apple-maps-api/month)](https://pepy.tech/project/apple-maps-api)
![GitHub CI Status](https://github.com/iloveitaly/apple-maps-api/actions/workflows/build_and_publish.yml/badge.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Python Client for Apple Maps Server API

A modern, type-safe Python client for the [Apple Maps Server API](https://developer.apple.com/documentation/applemapsserverapi).

## Why This Library?

I've always found Apple's documentation for the Maps Server API a bit opaque, especially when it comes to JWT management. I built this library to handle the heavy lifting: signing tokens, automatic refreshes, and providing a clean, type-safe interface for geocoding and search.

If you are building a server-side application that needs to interact with Apple's mapping services without the overhead of MapKit JS or a full mobile SDK, this is for you. It's built on top of Pydantic and `httpx`, so it's ready for modern Python workflows.

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

### Geocoding

Convert an address string to coordinates:

```python
results = client.geocode("1 Apple Park Way, Cupertino, CA")

for place in results.results:
    print(f"{place.name}: {place.coordinate.latitude}, {place.coordinate.longitude}")
```

### Reverse Geocoding

Convert coordinates back to a structured address:

```python
results = client.reverse_geocode(lat=37.3346, lon=-122.0090)

if results.results:
    print(results.results[0].formattedAddressLines)
```

### Place Search

Search for points of interest near a location:

```python
results = client.search("pizza", at="37.3346,-122.0090")

for place in results.results:
    print(f"{place.name} - {place.formattedAddressLines}")
```

### Address Autocomplete

Provide search completions for a partial query:

```python
results = client.autocomplete("1 Apple Park", at="37.3346,-122.0090")

for completion in results.results:
    print(completion.completionTitle)
```

### Helper Functions

The library includes high-level helpers for common geocoding operations:

```python
from apple_maps_api import geocode_postal_code, geocode_coordinates

# Geocode a postal code
result = geocode_postal_code(client, postal_code="95014", country="US")
if result:
    print(f"Coordinates: {result.lat}, {result.lon}")
    print(f"City: {result.city}")

# Reverse geocode coordinates
result = geocode_coordinates(client, lat=37.3346, lon=-122.0090)
if result:
    print(f"Postal Code: {result.postal_code}")
    print(f"State: {result.state_code}")
```

## API Reference

### AppleMapsClient Methods

- `geocode(query, country=None, lang=None)` - Convert address to coordinates
- `reverse_geocode(lat, lon, lang=None)` - Convert coordinates to address
- `search(query, at=None, bbox=None, country=None, lang=None)` - Search for places and POIs
- `autocomplete(query, at=None, bbox=None, country=None, lang=None)` - Provide search completions
- `create_token()` - Generate a MapKit JS compatible access token

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
