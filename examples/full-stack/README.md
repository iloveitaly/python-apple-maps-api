# Full-stack Apple Maps example

1. **`app/main.py`** — Server API demo via `AppleMapsClient`
2. **`app/server.py`** — FastAPI backend (`/api/maps-token`, `/api/autocomplete`)
3. **`web/`** — React UI: MapKit map + autocomplete page

## Prerequisites

```bash
export APPLE_MAPS_TEAM_ID=...
export APPLE_MAPS_KEY_ID=...
export APPLE_MAPS_P8_KEY=...   # PEM or raw base64 DER
```

## Setup

```bash
just setup
```

## Usage

```bash
just run   # exercise Server API endpoints
just dev   # FastAPI + UI at http://localhost:5173
```

- API docs: http://127.0.0.1:8765/docs
- **Map** — MapKit JS map (token from `create_mapkit_token()`)
- **Autocomplete** — input that calls `GET /api/autocomplete?q=…` → `client.autocomplete()`
