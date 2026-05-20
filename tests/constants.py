"""Shared constants for tests."""

# test-only placeholder key (non-sensitive)
TEST_PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
TEST-ONLY-PLACEHOLDER-KEY-NOT-FOR-USE
-----END PRIVATE KEY-----"""

TOKEN_RESPONSE = {
    "accessToken": "test_access_token",
    "expiresInSeconds": 1800,
}

SAMPLE_GEOCODE_RESPONSE = {
    "results": [
        {
            "name": "1 Apple Park Way",
            "coordinate": {"latitude": 37.3349, "longitude": -122.0090},
            "formattedAddressLines": ["1 Apple Park Way", "Cupertino, CA 95014"],
            "structuredAddress": {
                "locality": "Cupertino",
                "administrativeArea": "California",
                "administrativeAreaCode": "CA",
                "postCode": "95014",
                "fullThoroughfare": "1 Apple Park Way",
                "thoroughfare": "Apple Park Way",
                "subThoroughfare": "1",
            },
            "country": "United States",
            "countryCode": "US",
        }
    ]
}

SAMPLE_REVERSE_GEOCODE_RESPONSE = SAMPLE_GEOCODE_RESPONSE

SAMPLE_POSTAL_GEOCODE_RESPONSE = {
    "results": [
        {
            "name": "95014",
            "coordinate": {"latitude": 37.318, "longitude": -122.045},
            "formattedAddressLines": ["Cupertino, CA 95014"],
            "structuredAddress": {
                "locality": "Cupertino",
                "administrativeArea": "California",
                "administrativeAreaCode": "CA",
                "postCode": "95014",
            },
            "country": "United States",
            "countryCode": "US",
        }
    ]
}

SAMPLE_SEARCH_RESPONSE = {
    "results": [
        {
            "name": "Apple Park",
            "poiCategory": "Landmark",
            "coordinate": {"latitude": 37.3349, "longitude": -122.0090},
            "formattedAddressLines": ["1 Apple Park Way", "Cupertino, CA 95014"],
            "structuredAddress": {
                "locality": "Cupertino",
                "administrativeAreaCode": "CA",
            },
            "country": "United States",
            "countryCode": "US",
        }
    ],
    "displayMapRegion": {
        "northLatitude": 37.5,
        "southLatitude": 37.1,
        "eastLongitude": -121.7,
        "westLongitude": -122.5,
    },
}

SAMPLE_AUTOCOMPLETE_RESPONSE = {
    "results": [
        {
            "completionUrl": "/v1/search?q=1+Apple+Park+Way&metadata=abc",
            "displayLines": ["1 Apple Park Way", "Cupertino, CA"],
            "location": {"latitude": 37.3349, "longitude": -122.0090},
            "structuredAddress": {
                "locality": "Cupertino",
                "administrativeAreaCode": "CA",
            },
        }
    ]
}
