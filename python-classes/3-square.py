#!/usr/bin/python3
"""A class representing a square"""


class Square:
    def __init__(self, size=0):
        """Initialize a square object and validation"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """public instance method that return the current square area"""
        area = self.__size * self.__size
        return area
