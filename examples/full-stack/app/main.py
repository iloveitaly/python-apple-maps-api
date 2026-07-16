"""Exercise Apple Maps Server API endpoints via AppleMapsClient."""

from pydantic import BaseModel

from apple_maps_api import AppleMapsClient

# Cupertino area
NEAR = "37.3317,-122.0307"
# northLat,eastLng,southLat,westLng
REGION = "37.5,-121.7,37.1,-122.5"
APPLE_PARK = (37.334859, -122.0090403)


def show(title: str, result: BaseModel) -> None:
    print(f"\n{'=' * 60}\n  {title}\n{'=' * 60}")
    print(result.model_dump_json(indent=2))


def main() -> None:
    client = AppleMapsClient.from_env()

    ac = client.autocomplete("1 Apple Park")
    show("autocomplete", ac)

    if ac.results:
        show("search_completion", client.search_completion(ac.results[0]))

    show("search (near)", client.search("1 Apple Park Way", near=NEAR))
    show("search (region)", client.search("Apple Park", search_region=REGION))
    show(
        "search (user_location)",
        client.search("1 Apple Park Way", user_location=NEAR),
    )
    show("geocode", client.geocode("1 Apple Park Way, Cupertino, CA"))
    show("reverse_geocode", client.reverse_geocode(APPLE_PARK))


if __name__ == "__main__":
    main()
