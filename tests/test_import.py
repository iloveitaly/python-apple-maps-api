"""Test apple-maps-api."""

import apple_maps_api


def test_import() -> None:
    """Test that the  can be imported."""
    assert isinstance(apple_maps_api.__name__, str)


def test_version() -> None:
    """Test that the version is available."""
    assert isinstance(apple_maps_api.__version__, str)