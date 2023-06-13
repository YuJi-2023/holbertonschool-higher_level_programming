#!/usr/bin/python3
"""A class representing a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of square"""
        return self.__size

    @property
    def position(self):
        """Get the position of square"""
        return self.__position

    @size.setter
    def size(self, value):
        """Set the size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Set the position of square"""
        error_message = "position must be a tuple of 2 positive integers"
        if (type(value) != tuple or len(value) != 2):
            raise TypeError(error_message)
        for i in value:
            if type(i) != int or i < 0:
                raise TypeError(error_message)
        self.__position = value

    def area(self):
        """calculate and return the current square area"""
        return self.size ** 2

    def my_print(self):
        """ Print out the square"""
        if self.size == 0:
            print()
        else:
            for count in range(0, self.position[1]):
                print("")
            for i in range(0, self.size):
                print(" " * self.position[0], end="")
                print("#" * self.size)
