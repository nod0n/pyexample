"""Smoke tests for pyexample.models.baseline"""

import pyexample.models.baseline as baseline


def test_import():
    """Verify baseline module imports"""
    assert baseline is not None


def test_forward_exists():
    """Verify forward function exists"""
    assert callable(baseline.forward)
