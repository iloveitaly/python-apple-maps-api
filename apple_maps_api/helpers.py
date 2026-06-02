"""Helper functions for common geocoding operations."""

import logging
from typing import TYPE_CHECKING

from apple_maps_api.models import GeocodeResult, Place

if TYPE_CHECKING:
    from apple_maps_api.client import AppleMapsClient

log = logging.getLogger(__name__)


def _log_geocode_event(message: str, level: str = "info", **extras: object) -> None:
    extra_str = ", ".join(f"{k}={v!r}" for k, v in extras.items())
    full_message = f"{message} ({extra_str})" if extra_str else message
    getattr(log, level)(full_message)


def _place_to_geocode_result(
    place: Place,
    *,
    lat: float | None = None,
    lon: float | None = None,
    postal_code_override: str | None = None,
) -> GeocodeResult | None:
    """Extract a GeocodeResult from an Apple Maps Place object.

    Returns None if coordinates cannot be determined.
    """
    coord = place.coordinate

    if lat is not None and lon is not None:
        result_lat = lat
        result_lon = lon
    elif coord:
        result_lat = coord.latitude
        result_lon = coord.longitude
    else:
        return None

    addr = place.structuredAddress
    address1 = addr.fullThoroughfare if addr else None
    city = addr.locality if addr else None
    state_code = addr.administrativeAreaCode if addr else None
    postal_code = postal_code_override or (addr.postCode if addr else None)

    formatted_address = None
    if place.formattedAddressLines:
        formatted_address = ", ".join(place.formattedAddressLines)

    return GeocodeResult(
        lat=result_lat,
        lon=result_lon,
        address1=address1,
        postal_code=postal_code,
        city=city,
        state_code=state_code,
        country_code=place.countryCode,
        formatted_address=formatted_address,
    )


def geocode_postal_code(
    client: "AppleMapsClient",
    *,
    postal_code: str,
    country: str = "US",
) -> GeocodeResult | None:
    """Geocode a postal code and extract coordinates and address information.

    Args:
        client: AppleMapsClient instance to use for geocoding
        postal_code: The postal code to geocode
        country: Country code (default: "US")

    Returns:
        GeocodeResult with lat, lon, city, and state information.
        Returns None if geocoding fails.
    """
    location_result = client.geocode(postal_code, limit_to_countries=country)

    if len(location_result.results) == 0:
        _log_geocode_event(
            "no geocoding results for zip code",
            level="info",
            zip=postal_code,
            country=country,
        )

        return None

    if len(location_result.results) > 1:
        _log_geocode_event(
            "multiple geocoding results for zip code",
            zip=postal_code,
            results=len(location_result.results),
        )

    place = location_result.results[0]

    return _place_to_geocode_result(place, postal_code_override=postal_code)


def geocode_coordinates(
    client: "AppleMapsClient",
    *,
    lat: float,
    lon: float,
) -> GeocodeResult | None:
    """Reverse geocode coordinates and extract address information.

    Args:
        client: AppleMapsClient instance to use for geocoding
        lat: Latitude
        lon: Longitude

    Returns:
        GeocodeResult with lat, lon, zip_code, city, and state information.
        Returns None if geocoding fails.
    """
    location_result = client.reverse_geocode((lat, lon))

    if len(location_result.results) == 0:
        _log_geocode_event(
            "no geocoding results for coordinates",
            level="info",
            lat=lat,
            lon=lon,
        )

        return None

    if len(location_result.results) > 1:
        _log_geocode_event(
            "multiple geocoding results for coordinates",
            lat=lat,
            lon=lon,
            results=len(location_result.results),
        )

    place = location_result.results[0]

    # preserve the caller's coordinates, not whatever Apple rounded to
    return _place_to_geocode_result(place, lat=lat, lon=lon)
