#!/usr/bin/python3
"""A class representing a square"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """Initialize a square object and validate the size"""
        self.__size = size

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """calculate and return the current square area"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Print out the square"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for i in range(0, self.__size):
                print("#", end='')
            print()
