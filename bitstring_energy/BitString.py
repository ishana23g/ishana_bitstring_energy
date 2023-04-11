import math
import numpy as np

class BitString:
    """
    Simple class to implement a string of bits
    """

    def __init__(self, config: np.array =None, N: int =None) -> None:
        """
        Saves the list of bits that are either 0s and 1s

        Parameters
        ----------
        config : list
            list of 0s and 1s
        """
        if (config == None and N == None):
            raise ValueError("Either the bitstring or the number of spins must be defined")
        elif (N != None and config == None):
            self.n = N
            config = np.zeros(N)
        else:
            if (len(config) != N):
                raise ValueError("The length of the bitstring does not match the number of spins")
            self.n = len(config)
            self.config = config

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
            config = np.array(config)
        self.config = config

    def set_config(self, config: np.array) -> None:
        """
        call set_string
        """
        self.set_string(config)

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
            digits = int(math.log(num, 2)) + 1
        # the bin(num) gives a string of the form '0b*****'
        # the [2:] removes the '0b' from the string
        # the zfill(digits) adds 0s to the front of the string to make it the correct length
        self.string = np.array([int(digit) for digit in bin(num)[2:].zfill(digits)])


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
            return self.config == __o.config
        return False

    def return_array(self) -> np.array:
        """
        Returns the bitstring as a list of 0s and 1s

        Returns
        -------
        list
            list of '0's and '1's
        """
        return self.config
