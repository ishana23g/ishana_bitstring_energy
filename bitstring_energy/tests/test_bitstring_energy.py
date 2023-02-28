"""
Unit and regression test for the bitstring_energy package.
"""

# Import package, test suite, and other packages as needed
import sys

import pytest

import bitstring_energy


def test_bitstring_energy_imported():
    """Sample test, will always pass so long as import statement worked."""
    assert "bitstring_energy" in sys.modules
