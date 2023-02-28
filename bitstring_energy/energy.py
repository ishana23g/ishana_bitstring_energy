"""Provide the primary functions."""


def canvas(with_attribution=True):
    """
    Placeholder function to show example docstring (NumPy format).

    Replace this function and doc string for your own project.

    Parameters
    ----------
    with_attribution : bool, Optional, default: True
        Set whether or not to display who the quote is from.

    Returns
    -------
    quote : str
        Compiled string including quote and optional attribution.
    """

    quote = "The code is but a canvas to our imagination."
    if with_attribution:
        quote += "\n\t- Adapted from Henry David Thoreau"
    return quote

import math
import numpy as np
import networkx as nx

class BitString:
    """
    Simple class to implement a string of bits
    """
    def __init__(self, string):
        self.string = string

    def __str__(self) -> str: 
        bitString = ""
        for i in range(len(self.string)):
            bitString += str(self.string[i])
        return bitString

    def __len__(self) -> int: 
        return len(self.string)

    def flip(self, index: int) -> None:
        if (self.string[index] == 0):
            self.string[index] = 1
        else:
            self.string[index] = 0

    def set_string(self, string):
        self.string = string

    def on(self) -> int:
        return np.sum(self.string)
    
    def off(self) -> int:
        return len(self.string) - self.on()
    
    def int(self) -> int:
        bit_to_int = 0
        for (i, bit) in enumerate(self.string):
            if bit == 1:
                bit_to_int += 2**(len(self.string) - i - 1)
        return bit_to_int

    def set_int(self, num, digits=None):
        if (digits is None):
            digits = int(math.log2(num)) + 1
        self.string = [0] * digits
        for i in range(digits - 1, -1, -1):
            self.string[i] = num % 2
            num = num//2
    
    def __eq__(self, __o: object):
        if (isinstance(__o, BitString)):
            return self.string == __o.string
        return False

    def return_array(self):
        return self.string

def energy(bs: BitString, G: nx.Graph):
    """Compute energy of configuration, `bs`

        .. math::
            E = \\left<\\hat{H}\\right>

    Parameters
    ----------
    bs   : Bitstring
        input configuration
    G    : Graph
        input graph defining the Hamiltonian
    Returns
    -------
    energy  : float
        Energy of the input configuration
    """

    # convert bit string such that for 0 -> -1 and 1 -> 1
    array = np.array(bs.return_array())
    bitString = (array * 2) - 1

    energy = 0
    for (i, j) in G.edges: 
        energy += G.edges[i, j]['weight'] * bitString[i] * bitString[j]
    return energy


if __name__ == "__main__":
    # Do something if this file is invoked on its own
    print(canvas())
