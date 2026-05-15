import json
import os
import time

import jwt
import requests

BASE_URL = "https://maps-api.apple.com"

# Example data: Apple HQ in Cupertino, CA
QUERY = "1 Apple Park"                          # partial address for autocomplete
FULL_QUERY = "1 Apple Park Way"
GEOCODE_QUERY = "1 Apple Park Way, Cupertino, CA"  # geocode needs city/state to resolve
POI_QUERY = "Apple Park"      # POI name for searchRegion (searchRegion filters strictly by coordinates)
CUPERTINO = "37.3317,-122.0307"
# searchRegion bounding box covering the South Bay / Cupertino area
SF_BAY_REGION = {
    "searchRegion[northLatitude]": "37.5",
    "searchRegion[southLatitude]": "37.1",
    "searchRegion[eastLongitude]": "-121.7",
    "searchRegion[westLongitude]": "-122.5",
}


def get_auth_jwt() -> str:
    """Build the signed JWT used to authenticate against /v1/token."""
    key_path = os.environ["APPLE_MAPS_KEY_PATH"]
    key_id = os.environ["APPLE_MAPS_KEY_ID"]
    team_id = os.environ["APPLE_MAPS_TEAM_ID"]

    with open(key_path) as f:
        private_key = f.read()

    now = int(time.time())
    payload = {
        "iss": team_id,
        "iat": now,
        "exp": now + 180 * 24 * 60 * 60,  # 180 days
    }
    return jwt.encode(payload, private_key, algorithm="ES256", headers={"kid": key_id})


def get_access_token(auth_jwt: str) -> str:
    """Exchange the signed JWT for a short-lived Maps access token."""
    resp = requests.get(
        f"{BASE_URL}/v1/token",
        headers={"Authorization": f"Bearer {auth_jwt}"},
    )
    resp.raise_for_status()
    return resp.json()["accessToken"]


def autocomplete(token: str, **params) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/searchAutocomplete",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    resp.raise_for_status()
    return resp.json()


def geocode(token: str, address: str) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/geocode",
        headers={"Authorization": f"Bearer {token}"},
        params={"q": address},
    )
    resp.raise_for_status()
    return resp.json()


def reverse_geocode(token: str, lat: float, lng: float) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/reverseGeocode",
        headers={"Authorization": f"Bearer {token}"},
        params={"loc": f"{lat},{lng}"},
    )
    resp.raise_for_status()
    return resp.json()


def search(token: str, **params) -> dict:
    resp = requests.get(
        f"{BASE_URL}/v1/search",
        headers={"Authorization": f"Bearer {token}"},
        params=params,
    )
    resp.raise_for_status()
    return resp.json()


def follow_completion_url(token: str, completion_url: str) -> dict:
    # completionUrl is a path like /v1/search?...
    url = BASE_URL + completion_url if completion_url.startswith("/") else completion_url
    resp = requests.get(url, headers={"Authorization": f"Bearer {token}"})
    resp.raise_for_status()
    return resp.json()


def print_addresses(result: dict) -> None:
    results = result.get("results", [])
    if not results:
        print("  (no results)")
        return
    for r in results:
        # /v1/search returns formattedAddressLines; /v1/searchAutocomplete returns displayLines
        addr_lines = r.get("formattedAddressLines") or r.get("displayLines", [])
        name = r.get("name", "")
        line1 = addr_lines[0] if addr_lines else name
        line2 = addr_lines[1] if len(addr_lines) > 1 else ""
        locality = r.get("structuredAddress", {}).get("locality", "")
        print(f"  Line 1: {line1}")
        if line2:
            print(f"  Line 2: {line2}")
        if locality:
            print(f"  City:   {locality}")
        print()


def section(title: str) -> None:
    bar = "=" * 60
    print(f"\n{bar}")
    print(f"  {title}")
    print(bar)


def main() -> None:
    token = get_access_token(get_auth_jwt())

    # ex: autocomplete(token, q="street address",limitToCountries="US",resultTypeFilter="address")

    # 1. Autocomplete — shows completionUrl structure
    section("1. /v1/searchAutocomplete  q=\"1 Apple Park\"")
    ac_result = autocomplete(token, q=QUERY)
    print(json.dumps(ac_result, indent=2))

    # 2. Follow the first completionUrl from autocomplete
    completions = ac_result.get("results", [])
    if completions:
        completion_url = completions[0].get("completionUrl", "")
        section(f"2. Follow completionUrl → {completion_url}")
        search_result = follow_completion_url(token, completion_url)
        print(json.dumps(search_result, indent=2))
        print("\n--- Extracted address ---")
        print_addresses(search_result)
    else:
        section("2. Follow completionUrl")
        print("  (no completions returned in step 1, skipping)")

    # 3. /v1/search with searchLocation
    section(f"3. /v1/search  q=\"{FULL_QUERY}\"  searchLocation={CUPERTINO}")
    result = search(token, q=FULL_QUERY, searchLocation=CUPERTINO)
    print(json.dumps(result, indent=2))
    print("\n--- Extracted address ---")
    print_addresses(result)

    # 4. /v1/search with searchRegion (bounding box; uses POI query since searchRegion filters strictly by coordinates)
    region_desc = "northLat=37.5 southLat=37.1 eastLng=-121.7 westLng=-122.5"
    section(f"4. /v1/search  q=\"{POI_QUERY}\"  searchRegion [{region_desc}]")
    result = search(token, q=POI_QUERY, **SF_BAY_REGION)
    print(json.dumps(result, indent=2))
    print("\n--- Extracted address ---")
    print_addresses(result)

    # 5. /v1/search with userLocation
    section(f"5. /v1/search  q=\"{FULL_QUERY}\"  userLocation={CUPERTINO}")
    result = search(token, q=FULL_QUERY, userLocation=CUPERTINO)
    print(json.dumps(result, indent=2))
    print("\n--- Extracted address ---")
    print_addresses(result)


    # 6. /v1/geocode — address → coordinates
    section(f"6. /v1/geocode  q=\"{GEOCODE_QUERY}\"")
    result = geocode(token, GEOCODE_QUERY)
    print(json.dumps(result, indent=2))
    print("\n--- Extracted address ---")
    print_addresses(result)

    # 7. /v1/reverseGeocode — coordinates → address
    lat, lng = 37.334859, -122.0090403  # Apple Park campus
    section(f"7. /v1/reverseGeocode  lat={lat}  lng={lng}")
    result = reverse_geocode(token, lat, lng)
    print(json.dumps(result, indent=2))
    print("\n--- Extracted address ---")
    print_addresses(result)


if __name__ == "__main__":
    main()
