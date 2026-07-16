"""FastAPI backend for the example UI: MapKit tokens + autocomplete."""

from fastapi import FastAPI, Query
from pydantic import BaseModel

from apple_maps_api import AppleMapsClient
from apple_maps_api.models import SearchAutocompleteResponse

app = FastAPI(title="Apple Maps example")
client = AppleMapsClient.from_env()


class MapKitToken(BaseModel):
    token: str


@app.get("/api/maps-token")
def maps_token() -> MapKitToken:
    return MapKitToken(token=client.create_mapkit_token())


@app.get("/api/autocomplete")
def autocomplete(q: str = Query("")) -> SearchAutocompleteResponse:
    q = q.strip()
    if not q:
        return SearchAutocompleteResponse(results=[])

    return client.autocomplete(q)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8765)
