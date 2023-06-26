#!/usr/bin/python3
"""define sublass Rectangle"""
from models.base import Base


class Rectangle(Base):
    """subclass inherits class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialise data"""
        super().__init__(id)

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self):
        """set the value of width"""
        self.__width = width

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self):
        """set the value of height"""
        self.__height = height

    @property
    def x(self):
        """retrieve x"""
        return self.__x

    @x.setter
    def x(self):
        """set the value for x"""
        self.__x = x

    @property
    def y(self):
        """retrieve y"""
        return self.__y

    @y.setter
    def y(self):
        """set value for y"""
        self.__y = y
