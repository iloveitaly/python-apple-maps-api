#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

from apple_maps_api import AppleMapsClient

QUERY = "748 Boise Dr"
LAT = 39.7351
LNG = -105.0269


def main() -> None:
    client = AppleMapsClient.from_env()
    response = client.autocomplete(QUERY, lat=LAT, lng=LNG)

    for result in response.results:
        if not result.displayLines:
            continue

        print(", ".join(result.displayLines))


if __name__ == "__main__":
    main()
