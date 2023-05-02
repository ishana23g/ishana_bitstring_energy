"""
Unit and regression test for the bitstring_energy package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import bitstring_energy as bse
import numpy as np

def test_dunder_methods():
    bitString = bse.BitString(N=10)

    assert len(bitString) == 10, "The length of the bitstring should be 10"
    assert str(bitString) == "0000000000", f"The bitstring should be 0000000000, but we got {bitString}"
    bitString[0] = 1
    assert str(bitString) == "1000000000", f"The bitstring should be 1000000000, but we got {bitString}"
    bitString[0] = 0
    assert str(bitString) == "0000000000", f"The bitstring should be 0000000000, but we got {bitString}"
    assert 2**10 == bitString.n_dim, f"The number of dimensions should be 2^10, but we got {bitString.n_dim}"

    try:
        bitString[0] = 2 # should raise an error
    except Exception as e:
        assert isinstance(e, ValueError), f"Should raise a ValueError, but we got {e}"

    assert str(bitString) == "0000000000", f"The bitstring should be 0000000000, but we got {bitString}"

    bitString.set_int_config(10)
    config=np.array([0,0,0,0,0,0,1,0,1,0])
    bitString2 = bse.BitString(N=10)
    bitString2.set_config(config)
    assert bitString == bitString2, f"The bitstrings should be equal, but we got {bitString} and {bitString2}"


def test_methods():
    bitString = bse.BitString(N=10)

    bitString.flip(0)
    assert str(bitString) == "1000000000", f"The bitstring should be 1000000000, but we got {bitString}"

    bitString.flip(0)
    assert str(bitString) == "0000000000", f"The bitstring should be 0000000000, but we got {bitString}"

    bitString.set_string([1]*10)
    assert str(bitString) == "1111111111", f"The bitstring should be 1111111111, but we got {bitString}"

    assert bitString.on() == 10, f"The number of 1's should be 10, but we got {bitString.on()}"
    assert bitString.off() == 0, f"The number of 0's should be 0, but we got {bitString.off()}"
    
    bitString.flip(0)
    assert bitString.on() == 9, f"The number of 1's should be 9, but we got {bitString.on()}"
    assert bitString.off() == 1, f"The number of 0's should be 1, but we got {bitString.off()}"

    bitString.set_int_config(10)
    assert str(bitString) == "0000001010", f"The bitstring should be 1010, but we got {bitString}"

    bitString.set_string([1,0,1,0,1])
    bitString_int = bitString.int()
    assert bitString_int == 21, f"The bitstring should be 21, but we got {bitString_int}"

    bs_array = bitString.return_array()
    assert np.array_equal(bs_array, np.array([1,0,1,0,1])), f"The array should be [1,0,1,0,1], but we got {bs_array}"

    bs_int = bitString.int()
    assert bs_int == 21, f"The bitstring should be 21, but we got {bs_int}"