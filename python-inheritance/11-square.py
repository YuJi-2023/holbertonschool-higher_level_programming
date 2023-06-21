#!/usr/bin/python3
"""Square class inherits Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a subclass to Rectangle"""

    def __init__(self, size):
        """initialise subclass with size"""
        self.__size = size
        super().integer_validator('size', size)

    def area(self):
        """implement area() method"""
        return self.__size * self.__size

    def __str__(self):
        """str() return a formated string representation of the rectangle"""
        return f"[Square] {self.__size}/{self.__size}"
