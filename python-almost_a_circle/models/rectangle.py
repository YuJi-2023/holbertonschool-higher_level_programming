#!/usr/bin/python3
"""define sublass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """subclass inherits class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise data"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the value of width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the value of height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the value for x"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set value for y"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area method that returns the area value of rectangle"""
        return self.__width * self.__height
