#!/usr/bin/python3
"""Square class"""


class Square:
    """Initializes data"""
    def __init__(self, size=0):
        """check size validation"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
