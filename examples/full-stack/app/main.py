"""Exercise Apple Maps Server API endpoints via AppleMapsClient."""

from pydantic import BaseModel

from apple_maps_api import AppleMapsClient, MapRegion

# Cupertino area
LAT = 37.3317
LNG = -122.0307
REGION = MapRegion(
    northLatitude=37.5,
    eastLongitude=-121.7,
    southLatitude=37.1,
    westLongitude=-122.5,
)
APPLE_PARK_LAT = 37.334859
APPLE_PARK_LNG = -122.0090403


def show(title: str, result: BaseModel) -> None:
    print(f"\n{'=' * 60}\n  {title}\n{'=' * 60}")
    print(result.model_dump_json(indent=2))


def main() -> None:
    client = AppleMapsClient.from_env()

    ac = client.autocomplete("1 Apple Park")
    show("autocomplete", ac)

    if ac.results:
        show("search_completion", client.search_completion(ac.results[0]))

    show("search (lat/lng)", client.search("1 Apple Park Way", lat=LAT, lng=LNG))
    show("search (region)", client.search("Apple Park", search_region=REGION))
    show(
        "search (user lat/lng)",
        client.search("1 Apple Park Way", user_lat=LAT, user_lng=LNG),
    )
    show("geocode", client.geocode("1 Apple Park Way, Cupertino, CA"))
    show(
        "reverse_geocode",
        client.reverse_geocode(lat=APPLE_PARK_LAT, lng=APPLE_PARK_LNG),
    )


if __name__ == "__main__":
    main()
