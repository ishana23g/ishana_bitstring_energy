import math
import numpy as np


class BitString:
    """
    Simple class to implement a string of bits
    """

    def __init__(self, list_of_bits: list):
        """
        Saves the list of bits that are either 0s and 1s

        Parameters
        ----------
        list_of_bits : list
            list of 0s and 1s
        """
        self.list_of_bits = list_of_bits

    def __str__(self) -> str:
        """
        Prints out the bitstring

        Returns
        -------
        bitString : str
            string of bits
        """
        bitString = ""
        for i in range(len(self.list_of_bits)):
            bitString += str(self.list_of_bits[i])
        return bitString

    def __len__(self) -> int:
        """
        Returns the number of bits present in the bitstring

        Returns
        -------
        length : int
            number of bits in the bitstring
        """
        return len(self.list_of_bits)

    def flip(self, index: int) -> None:
        """
        Flips the bit at the given index
        
        Parameters
        ----------
        index : int
            index of the bit to flip
        """
        if self.list_of_bits[index] == 0:
            self.list_of_bits[index] = 1
        else:
            self.list_of_bits[index] = 0

    def set_string(self, list_of_bits: list) -> None:
        """
        Sets the bitstring to the given list of bits
        """
        self.list_of_bits = list_of_bits

    def on(self) -> int:
        """
        Returns the number of '1's in the bitstring

        Returns
        -------
        on : int
            number of '1's in the bitstring
        """
        return np.sum(self.list_of_bits)

    def off(self) -> int:
        """
        Returns the number of '0's in the bitstring

        Returns
        -------
        off : int
            number of '0's in the bitstring
        """
        return len(self.list_of_bits) - self.on()

    def int(self) -> int:
        """
        Returns the integer value of the bitstring

        Returns
        -------
        bit_to_int : int
            integer value of the bitstring
        """
        bit_to_int = 0
        for (i, bit) in enumerate(self.list_of_bits):
            if bit == 1:
                bit_to_int += 2 ** (len(self.list_of_bits) - i - 1)
        return bit_to_int

    def set_int(self, num: int, digits: int =None) -> None:
        """
        Sets the bitstring to the given integer value
        
        Parameters
        ----------
        num : int
            integer value to set the bitstring to
        digits : int
            number of digits in the bitstring
        """
        if digits is None:
            digits = int(math.log2(num)) + 1
        self.list_of_bits = [0] * digits
        for i in range(digits - 1, -1, -1):
            self.list_of_bits[i] = num % 2
            num = num // 2

    def __eq__(self, __o: object) -> bool:
        """
        Checks if two bitstrings are equal
        
        Parameters
        ----------
        __o : object    
            object to compare to
        
        Returns
        -------
        bool
            True if the two bitstrings are equal, False otherwise
        """
        if isinstance(__o, BitString):
            return self.list_of_bits == __o.list_of_bits
        return False

    def return_array(self) -> list:
        """
        Returns the bitstring as a list of 0s and 1s

        Returns
        -------
        list
            list of '0's and '1's
        """
        return self.list_of_bits
