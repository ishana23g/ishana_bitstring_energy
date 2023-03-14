"""
Unit and regression test for the bitstring_energy package.
"""

# Import package, test suite, and other packages as needed
import sys
import pytest
import bitstring_energy as bse


def test_bitstring():
    bitString = bse.BitString([0]*10)

    assert len(bitString) == 10, "The length of the bitstring should be 10"
    assert str(bitString) == "0000000000", f"The bitstring should be 0000000000, but we got {bitString}"

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

    bitString.set_int(10)
    assert str(bitString) == "1010", f"The bitstring should be 1010, but we got {bitString}"

    bitString.set_string([1,0,1,0,1])
    bitString_int = bitString.int()
    assert bitString_int == 21, f"The bitstring should be 21, but we got {bitString_int}"

    bitString.set_int(10)
    bitString2 = bse.BitString([1,0,1,0])
    assert bitString == bitString2, f"The bitstrings should be equal, but we got {bitString} and {bitString2}"