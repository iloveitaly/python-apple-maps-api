# Examples

Canonical runnable examples live under [`examples/`](https://github.com/iloveitaly/python-apple-maps-api/tree/master/examples) and [`playground/`](https://github.com/iloveitaly/python-apple-maps-api/tree/master/playground). Docs stay in sync with code via `literalinclude`.

## Address Autocomplete

Minimal script: load credentials from the environment, autocomplete a query with a lat/lng bias, and print display lines.

```{literalinclude} ../playground/address_autocomplete.py
:language: python
```

Run it locally:

```bash
just examples
# or: uv run python playground/address_autocomplete.py
```

## Server API Demo

Exercise geocode, reverse geocode, search, autocomplete, and related endpoints via `AppleMapsClient`:

```{literalinclude} ../examples/full-stack/app/main.py
:language: python
```

## Full-stack FastAPI Backend

Mint MapKit JS tokens and proxy autocomplete for a React UI — see [`examples/full-stack/`](https://github.com/iloveitaly/python-apple-maps-api/tree/master/examples/full-stack):

```{literalinclude} ../examples/full-stack/app/server.py
:language: python
```
