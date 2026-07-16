"""Serve MapKit JS tokens via AppleMapsClient.create_mapkit_token()."""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer

from apple_maps_api import AppleMapsClient

client = AppleMapsClient.from_env()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self) -> None:
        if self.path.rstrip("/") != "/api/maps-token":
            self.send_error(404)
            return

        body = json.dumps({"token": client.create_mapkit_token()}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    print("MapKit token server: http://127.0.0.1:8765/api/maps-token")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
