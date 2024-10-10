"""
Tests for the ``json_errors`` module.
"""

from json_errors import __version__


def test_version() -> None:
    """
    The version number is what we expect.
    """
    assert __version__ == "0.0.1"
