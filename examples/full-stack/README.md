# Full-stack Apple Maps example

1. **`app/main.py`** — Server API demo via `AppleMapsClient`
2. **`app/token_server.py`** — MapKit JS tokens via `create_mapkit_token()`
3. **`web/`** — React + MapKit map that loads a token from the Python server

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
just dev   # token server + map UI at http://localhost:5173
```
