#!/usr/bin/env -S uv tool run ipython -i

from apple_maps_api.client import AppleMapsClient

client = AppleMapsClient.from_env()
