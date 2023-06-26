#!/usr/bin/python3
"""define sublass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """subclass inherits class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise data"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self, width):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, width):
        """set the value of width"""
        self.__width = width

    @property
    def height(self, height):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the value of height"""
        self.__height = height

    @property
    def x(self, x):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the value for x"""
        self.__x = x

    @property
    def y(self, y):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set value for y"""
        self.__y = y
