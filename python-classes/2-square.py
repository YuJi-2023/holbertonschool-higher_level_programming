#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """Initializes with size"""
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
