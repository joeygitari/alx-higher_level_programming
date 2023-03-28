#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Represents a square.
    Private instance attribute: size. 
    Instantiation with size (no type/value verification).
    """

    def __init__(self, size):
        """Initializes the square."""
        self.__size = size
