#!/usr/bin/python3
"""A class representing a square"""


class Square:
    """Square class"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square object"""
        self.__size = size
        self.__position = position

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
        if isinstance(value, tuple) and len(value) == 2 \
                and value[0] > 0 and value[1] > 0:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """calculate and return the current square area"""
        area = self.__size * self.__size
        return area

    def my_print(self):
        """ Print out the square"""
        if self.__size == 0:
            print()
        else:
            for count in range(0, self.__position[1]):
                print('')
            for i in range(0, self.__size):
                print(' '*self.__position[0], end='')
                print("#"*self.__size)
