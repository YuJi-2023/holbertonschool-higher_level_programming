#!/usr/bin/python3
"""Rectangle class inherits BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a subclass to BaseGeometry"""

    def __init__(self, width, height):
        """initialise subclass with width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)
