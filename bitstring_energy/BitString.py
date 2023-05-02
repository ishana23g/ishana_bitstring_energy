import math
import numpy as np
import random

class BitString:
    """
    Simple class to implement a string of bits
    """

    def __init__(self, N: int =None) -> None:
        """
        Saves the list of bits that are either 0s and 1s

        Parameters
        ----------
        N : int
            number of spins
        
        Raises
        ------
        AttributeError :
            if neither the bitstring or the number of spins are defined
        """        
        if (N == None):
            raise AttributeError("Must define the number of spins")
        else:
            self.n = N
            self.config = np.zeros(N, dtype=int)
            self.n_dim = 2**self.n


    def __str__(self) -> str:
        """
        Prints out the bitstring

        Returns
        -------
        bitString : str
            string of bits
        """
        return ''.join([str(i) for i in self.config])

    def __len__(self) -> int:
        """
        Returns the number of bits present in the bitstring

        Returns
        -------
        length : int
            number of bits in the bitstring
        """
        return len(self.config)
    
    def __getitem__(self, index: int) -> int:
        """
        Returns the bit at the given index

        Parameters
        ----------
        index : int
            index of the bit to return

        Returns
        -------
        bit : int
            bit at the given index
        """
        return self.config[index]

    def __setitem__(self, index: int, value: int) -> None:
        """
        Sets the bit at the given index

        Parameters
        ----------
        index : int
            index of the bit to set
        value : int
            value to set the bit to
        
        Raises
        ------
        ValueError :
            if the value is not 0 or 1
        """
        value = int(value) 
        if (value != 0 and value != 1):
            raise ValueError("The value must be 0 or 1")
        self.config[index] = value

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
            for i in range(self.n):
                if (self[i] != __o[i]):
                    return False
            return True
        return False

    def flip(self, index: int) -> None:
        """
        Flips the bit at the given index
        
        Parameters
        ----------
        index : int
            index of the bit to flip
        """
        self.config[index] = 1 - self.config[index]
    
    def set_string(self, config: np.array) -> None:
        """
        Sets the bitstring to the given list of bits
        """
        if (type(config) != np.ndarray):
            config = np.array(config, dtype=int)
        self.config = np.array(config, dtype=int)

    def set_config(self, config: np.array) -> None:
        """
        call set_string
        """
        self.set_string(np.array(config, dtype=int))

    def on(self) -> int:
        """
        Returns the number of '1's in the bitstring

        Returns
        -------
        on : int
            number of '1's in the bitstring
        """
        return np.sum(self.config)

    def off(self) -> int:
        """
        Returns the number of '0's in the bitstring

        Returns
        -------
        off : int
            number of '0's in the bitstring
        """
        return len(self.config) - self.on()

    def int(self) -> int:
        """
        Returns the integer value of the bitstring

        Returns
        -------
        bit_to_int : int
            integer value of the bitstring
        """
        bit_to_int = 0
        for digit in self.config:
            bit_to_int = (bit_to_int << 1) | int(digit)
        return bit_to_int

    def set_int_config(self, num: int, digits: int =None) -> None:
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
            digits = self.n
        # the bin(num) gives a string of the form '0b*****'
        # the [2:] removes the '0b' from the string
        # the zfill(digits) adds 0s to the front of the string to make it the correct length
        self.config = np.array([int(digit) for digit in bin(num)[2:].zfill(digits)], dtype=int)

    def return_array(self) -> np.array:
        """
        Returns the bitstring as a list of 0s and 1s

        Returns
        -------
        list
            list of '0's and '1's
        """
        return self.config
    
    def initialize(self, M=0, verbose=0):
        """
        Initialize spin configuration with specified magnetization
        
        Parameters
        ----------
        M   : Int, default: 0
            Total number of spin up sites 
        """
        self.config = np.zeros(self.n, dtype=int) 
        random_list = random.sample(range(0, self.n), M)
        for i in random_list:
            self.config[i] = 1
