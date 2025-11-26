"""Smoke tests for pyexample.utils.data"""

import pyexample.utils.data as data


def test_import():
    """Verify data module imports"""
    assert data is not None


def test_prepare_data_exists():
    """Verify prepare_data function exists"""
    assert callable(data.prepare_data)


def test_load_returns_dataframe():
    """Verify load function returns DataFrame"""
    df = data.load()
    assert df is not None
