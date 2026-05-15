Based on the investigation into the codebase, here is a concise summary of the top-level calls to the Radar API and the data structures used for their inputs and outputs.

### Top-Level Radar API Calls

The application integrates with the `radar-mapping-api` package, initializing a `RadarClient` globally (`app/configuration/radar.py`) and wrapping it in utility functions. 

1. **Autocomplete Address**
   - **Call:** `radar_client.autocomplete(query, country_code, layers)`
   - **Purpose:** Returns address suggestions for a partial query string (e.g., used in public geolocation routes).
   - **Input:** `query` (string), `country_code` (string, e.g., 'US'), `layers` (string/list, e.g., 'address').
   - **Output:** Returns a list of **`Address`** objects.

2. **Reverse Geocode**
   - **Call:** `radar_client.reverse_geocode(coordinates)`
   - **Purpose:** Returns address details for specific latitude and longitude coordinates. Used for finding theater addresses and public reverse geocode routes.
   - **Input:** `coordinates` (tuple or string of `lat, lon`).
   - **Output:** Returns a list of **`Address`** objects.

3. **Search Places (Theaters)**
   - **Call:** `radar_client.search_places(near, categories, radius)`
   - **Purpose:** Searches for nearby places within a radius (max 10km). Specifically used to query the `'movie-theatre'` category to find nearby theaters.
   - **Input:** `near` (coordinates `lat,lon`), `categories` (string, e.g., `'movie-theatre'`), `radius` (integer distance).
   - **Output:** Returns a list of **`Place`** objects.

4. **Forward Geocode**
   - **Call:** *Via custom helpers* like `geocode_postal_code(radar_client, postal_code)` and `geocode_coordinates(radar_client, lat, lon)`.
   - **Purpose:** Resolves user-provided zip codes or coordinates into standardized location metadata.
   - **Input:** Zip codes or coordinates.
   - **Output:** Returns an internal **`GeocodeResult`** model.

### Key Data Structures

**Inputs (Arguments):**
- **Coordinates:** Typically expected as a string `"lat,lon"` or tuple/list.
- **Postal Code:** Standard string format.
- **Queries/Filters:** Strings such as `"movie-theatre"` for categories, or partial text strings for autocomplete.

**Outputs (Radar Objects & Internal Wrappers):**
- **`Address` (from Radar):** Contains detailed location data: `formattedAddress`, `street`, `number`, `city`, `state`, `stateCode`, `postalCode`, `latitude`, and `longitude`.
- **`Place` (from Radar):** Represents a physical establishment. Contains `name`, `location` (GeoJSON point), `chain` (with `name`), and `categories`.
- **`GeocodeResult` (Internal Pydantic Model):** A simplified mapping from Radar's responses containing `lat`, `lon`, `city`, `state_code`, and `postal_code`.
- **`TheaterLocation` (Internal Pydantic Model):** A custom model that wraps a Radar `Place` and `Address` together, supplementing it with a calculated `distance`.
- **`GeolocationPoint` (Internal Pydantic Model):** Has a `.from_radar_address()` constructor to map Radar's raw `Address` properties into the app's internal point representation.