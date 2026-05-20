"""Integration tests for create_mapkit_token() against real credentials.

These tests require the following environment variables to be set:
- APPLE_MAPS_TEAM_ID
- APPLE_MAPS_KEY_ID
- APPLE_MAPS_P8_KEY
"""

import os
import time

import jwt
import pytest
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from apple_maps_api import AppleMapsClient


@pytest.fixture
def credentials() -> dict[str, str]:
    team_id = os.environ.get("APPLE_MAPS_TEAM_ID", "")
    key_id = os.environ.get("APPLE_MAPS_KEY_ID", "")
    private_key = os.environ.get("APPLE_MAPS_P8_KEY", "")

    if not all([team_id, key_id, private_key]):
        pytest.skip("Apple Maps env vars not set")

    return {"team_id": team_id, "key_id": key_id, "private_key": private_key}


@pytest.fixture
def public_key(credentials: dict[str, str]):
    pem = credentials["private_key"].strip()
    if not pem.startswith("-----BEGIN"):
        pem = f"-----BEGIN PRIVATE KEY-----\n{pem}\n-----END PRIVATE KEY-----"
    private_key_obj = load_pem_private_key(pem.encode(), password=None)
    return private_key_obj.public_key()


class TestMapKitTokenIntegration:
    def test_returns_three_part_jwt(self, credentials: dict[str, str]):
        client = AppleMapsClient(**credentials)
        token = client.create_mapkit_token()
        assert token.count(".") == 2

    def test_header_alg_and_kid(self, credentials: dict[str, str]):
        client = AppleMapsClient(**credentials)
        token = client.create_mapkit_token()
        header = jwt.get_unverified_header(token)
        assert header["alg"] == "ES256"
        assert header["kid"] == credentials["key_id"]

    def test_signature_valid(self, credentials: dict[str, str], public_key):
        client = AppleMapsClient(**credentials)
        token = client.create_mapkit_token()
        # raises DecodeError / InvalidSignatureError if invalid
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["iss"] == credentials["team_id"]

    def test_claims_iss_iat_exp(self, credentials: dict[str, str], public_key):
        before = int(time.time())
        client = AppleMapsClient(**credentials)
        token = client.create_mapkit_token()
        after = int(time.time())

        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["iss"] == credentials["team_id"]
        assert before <= claims["iat"] <= after
        assert claims["exp"] > after

    def test_no_origin_claim_by_default(self, credentials: dict[str, str], public_key):
        client = AppleMapsClient(**credentials)
        token = client.create_mapkit_token()
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert "origin" not in claims

    def test_origin_claim_included_when_set(
        self, credentials: dict[str, str], public_key
    ):
        client = AppleMapsClient(**credentials, origin="https://example.com")
        token = client.create_mapkit_token()
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["origin"] == "https://example.com"

    def test_successive_calls_produce_different_tokens(
        self, credentials: dict[str, str]
    ):
        client = AppleMapsClient(**credentials)
        t1 = client.create_mapkit_token()
        time.sleep(1)
        t2 = client.create_mapkit_token()
        # iat differs by at least 1s so the signed output must differ
        assert t1 != t2
