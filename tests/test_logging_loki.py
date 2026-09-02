"""Tests for logging_loki."""

from logging_loki import __version__


def test_version() -> None:
    """Test that version is defined."""
    assert __version__ is not None
    assert isinstance(__version__, str)
