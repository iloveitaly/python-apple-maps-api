# Setting Up MapKit JS Credentials

Practical guide for creating the Apple Developer credentials needed by MapKit JS (web) and this library’s Server API client.

Based on setup notes written July 2026, adapted from the [Create with Swift MapKit JS tutorial](https://www.createwithswift.com/using-mapkit-js-to-embed-apple-maps-in-websites/) and Apple’s current Developer portal flow.

> **Note:** Third-party tutorials often still point at Apple’s old `maps.developer.apple.com/token-maker` page. That flow has moved into the [Apple Developer](https://developer.apple.com/account) portal. Prefer the steps below over outdated token-maker screenshots.

## What You Need

This library and MapKit JS need three values from your Apple Developer account:

| Env var              | What it is                                          |
|----------------------|-----------------------------------------------------|
| `APPLE_MAPS_TEAM_ID` | Your Apple Developer Team ID (Membership details)   |
| `APPLE_MAPS_KEY_ID`  | Auto-generated Key ID for the MapKit JS private key |
| `APPLE_MAPS_P8_KEY`  | Contents of the downloaded `.p8` private key (PEM)  |

Optional:

| Env var             | What it is                                                                              |
|---------------------|-----------------------------------------------------------------------------------------|
| `APPLE_MAPS_ORIGIN` | Domain restriction baked into JWTs minted by this client (e.g. `http://localhost:5173`) |

See [`.env-example`](../.env-example) and the README.

## Credential Types (Quick Reference)

Apple’s portal uses several similar-sounding names. Only some are required for a JS web + Python client setup:

| Term              | What it is                                                                                                  | Editable later?                                                                                               |
|-------------------|-------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| **Maps ID**       | Identifier that labels an environment/app for MapKit JS (reverse-domain style, e.g. `maps.com.example.app`) | Description only — the **identifier string cannot be renamed**. Wrong value → delete/recreate.                |
| **MapKit JS Key** | Private key (`.p8`) associated with MapKit JS + a Maps ID                                                   | Can be revoked; private key is downloadable **once**                                                          |
| **Key ID**        | Apple-generated ID for that key (not something you invent)                                                  | Fixed at creation                                                                                             |
| **Team ID**       | Your Apple Developer team                                                                                   | From Membership                                                                                               |
| **Token (JWT)**   | Signed token used by MapKit JS in the browser (or by the Server API)                                        | Domain restrictions / settings for portal tokens are editable; JWTs you mint yourself expire and are replaced |

For this repo you typically:

1. Create a **Maps ID**
2. Create a **MapKit JS Key** tied to that Maps ID
3. Store Team ID + Key ID + `.p8` contents as env vars
4. Mint JWTs with `AppleMapsClient.create_mapkit_token()` (preferred) instead of a one-off portal token maker

## Costs and Limits

Recreating or deleting Maps IDs / keys / tokens does **not** by itself incur extra charges, usage penalties, or credit loss. You are not billed for correcting a typo in a Maps ID.

(Usage of Maps itself is subject to Apple’s Maps pricing/quotas — that is separate from creating credentials.)

## Setup Steps (Current Developer Portal)

### 1. Create a Maps ID

1. Sign in at [developer.apple.com/account](https://developer.apple.com/account).
2. Open **Certificates, Identifiers & Profiles** → **Identifiers**.
3. Click **+** → select **Maps IDs** → Continue.
4. Enter:
   - **Description** — human-readable label (project/app name). Can be clarified later if the UI allows editing description.
   - **Identifier** — reverse-domain style starting with `maps.`, e.g. `maps.com.yourcompany.yourapp`. **This cannot be renamed after creation.**
5. Review → **Register**.

Tips:

- Use separate Maps IDs (and keys) for development vs production when practical, so revoking a compromised prod key does not break local/dev.
- Double-check the identifier spelling before registering.

### 2. Create a MapKit JS private key

1. Same portal section → **Keys** → **+**.
2. Name the key.
3. Enable **MapKit JS** (requires at least one Maps ID to exist).
4. Click **Configure**, choose the Maps ID from step 1, Save.
5. Continue → Register.
6. **Download the `.p8` immediately** and store it securely. Apple only allows one download.
7. Copy the **Key ID** shown for the key (auto-generated).

Never put the `.p8` private key in frontend/public code. Only JWTs derived from it should reach the browser.

### 3. Configure allowed domains (portal / token restrictions)

When restricting where a MapKit JS token may be used:

- You can list **multiple domains** on the same MapKit JS token/configuration.
- Domain fields are format-sensitive.
- Do **not** include `http://` or `https://` prefixes if the field expects a bare host (follow the portal field’s current format hints).
- Typos in allowed domains will silently block the map from loading on that host — re-check spelling.
- Domain restrictions and related token settings **can be edited after creation**.

#### Local development: `localhost` vs `127.0.0.1`

- `localhost` and `127.0.0.1` both refer to your local machine, but they are different host strings for origin/domain matching.
- Apple’s domain field may accept `localhost` and reject `127.0.0.1` (or vice versa) depending on current validation.
- Match the host you actually open in the browser (`http://localhost:5173` vs `http://127.0.0.1:5173`).

For this library, domain locking for minted JWTs is done via `APPLE_MAPS_ORIGIN` / `origin=` on `AppleMapsClient` (full origin including scheme and port when needed, e.g. `http://localhost:5173`). Omit `origin` for unrestricted local experiments.

Wildcard / multi-domain behavior should be verified against Apple’s current portal UI — multiple explicit domains under one token configuration is supported.

### 4. Wire credentials into this project

```bash
export APPLE_MAPS_TEAM_ID=...
export APPLE_MAPS_KEY_ID=...
export APPLE_MAPS_P8_KEY="-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----"
# optional MapKit JS origin lock:
# export APPLE_MAPS_ORIGIN=http://localhost:5173
```

Mint a MapKit JS JWT:

```python
from apple_maps_api import AppleMapsClient

client = AppleMapsClient.from_env()
token = client.create_mapkit_token()  # short-lived; fine for token endpoints
```

For local frontend work only, a longer TTL is available (do not ship long-lived tokens in production builds):

```python
token = client.create_mapkit_token(ttl_seconds=30 * 24 * 60 * 60)
```

Runnable MapKit JS + autocomplete example: [`examples/full-stack/`]().

## Troubleshooting Checklist

| Symptom                                      | Likely cause                                                                              |
|----------------------------------------------|-------------------------------------------------------------------------------------------|
| Map never initializes / authorization errors | Wrong Team ID, Key ID, or `.p8`; JWT expired; origin mismatch                             |
| Works on one URL but not another             | Allowed domains / `origin` claim does not match the page host (`localhost` ≠ `127.0.0.1`) |
| Cannot find token-maker page from a tutorial | Flow moved into Developer portal; mint JWTs here with `create_mapkit_token()`             |
| Lost `.p8` file                              | Create a new MapKit JS key (old key can be revoked); private keys are one-time download   |
| Mistyped Maps ID identifier                  | Cannot rename — create a new Maps ID (no penalty for recreation)                          |

## Official References

- [Creating a Maps identifier and a private key](https://developer.apple.com/documentation/applemapsserverapi/creating-a-maps-identifier-and-a-private-key) (mirrored under [`docs/apple_maps_documentation/`]())
- [Creating and using tokens with Maps Server API](https://developer.apple.com/documentation/applemapsserverapi/creating-and-using-tokens-with-maps-server-api)
- [MapKit JS](https://developer.apple.com/maps/mapkitjs/)
- Tutorial used during initial setup (partially outdated on token generation UI): [Using MapKit JS to Embed Apple Maps in Websites](https://www.createwithswift.com/using-mapkit-js-to-embed-apple-maps-in-websites/)
