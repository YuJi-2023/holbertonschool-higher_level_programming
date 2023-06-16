#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """initialise data"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieve the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """calculate and return the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """calculate and return the rectangle perimeter"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return (self.width + self.height) * 2

    @classmethod
    def create_rec(cls, row, col):
        """create a classmethod to return rectangle with #"""
        new_rec = []
        for _ in range(col):
            row_list = list('#' * row)
            new_rec.append(row_list)
        return new_rec

    def __str__(self):
        """define a custom __str__()"""
        return '\n'.join(''.join(row) for row in self.create_rec(self.width,
                         self.height))
