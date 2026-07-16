"""Integration tests for create_mapkit_token() against real credentials.

These tests require the following environment variables to be set:
- APPLE_MAPS_TEAM_ID
- APPLE_MAPS_KEY_ID
- APPLE_MAPS_P8_KEY
"""

import time

import jwt
import pytest
from cryptography.hazmat.primitives.serialization import load_pem_private_key

from apple_maps_api import AppleMapsClient


@pytest.fixture
def apple_client() -> AppleMapsClient:
    return AppleMapsClient.from_env()


# TODO can we document the purpose of this in a docstr?
@pytest.fixture
def public_key(apple_client: AppleMapsClient):
    pem = apple_client.private_key.strip()
    if not pem.startswith("-----BEGIN"):
        pem = f"-----BEGIN PRIVATE KEY-----\n{pem}\n-----END PRIVATE KEY-----"
    private_key_obj = load_pem_private_key(pem.encode(), password=None)
    return private_key_obj.public_key()


class TestMapKitTokenIntegration:
    def test_returns_three_part_jwt(self, apple_client: AppleMapsClient):
        token = apple_client.create_mapkit_token()
        assert token.count(".") == 2

    def test_header_alg_and_kid(self, apple_client: AppleMapsClient):
        token = apple_client.create_mapkit_token()
        header = jwt.get_unverified_header(token)
        assert header["alg"] == "ES256"
        assert header["kid"] == apple_client.key_id

    def test_signature_valid(self, apple_client: AppleMapsClient, public_key):
        token = apple_client.create_mapkit_token()
        # raises DecodeError / InvalidSignatureError if invalid
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["iss"] == apple_client.team_id

    def test_claims_iss_iat_exp(self, apple_client: AppleMapsClient, public_key):
        before = int(time.time())
        token = apple_client.create_mapkit_token()
        after = int(time.time())

        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["iss"] == apple_client.team_id
        assert before <= claims["iat"] <= after
        assert claims["exp"] - claims["iat"] == 60 * 60
        assert claims["exp"] > after

    def test_custom_ttl(self, apple_client: AppleMapsClient, public_key):
        ttl_seconds = 2 * 60 * 60
        token = apple_client.create_mapkit_token(ttl_seconds=ttl_seconds)
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["exp"] - claims["iat"] == ttl_seconds

    def test_no_origin_claim_by_default(self, apple_client: AppleMapsClient, public_key):
        token = apple_client.create_mapkit_token()
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert "origin" not in claims

    def test_origin_claim_included_when_set(
        self, apple_client: AppleMapsClient, public_key
    ):
        client = AppleMapsClient(
            team_id=apple_client.team_id,
            key_id=apple_client.key_id,
            private_key=apple_client.private_key,
            origin="https://example.com",
        )
        token = client.create_mapkit_token()
        claims = jwt.decode(token, public_key, algorithms=["ES256"])
        assert claims["origin"] == "https://example.com"

    def test_successive_calls_produce_different_tokens(
        self, apple_client: AppleMapsClient
    ):
        t1 = apple_client.create_mapkit_token()
        time.sleep(1)
        t2 = apple_client.create_mapkit_token()
        # iat differs by at least 1s so the signed output must differ
        assert t1 != t2
