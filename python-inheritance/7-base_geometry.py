#!/usr/bin/python3
"""BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """public method area()"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates value"""
        msg_1 = f"{name} must be an integer"
        msg_2 = f"{name} must be greater than 0"
        if  type(value) != int:
            raise TypeError(msg_1)
        if value <= 0:
            raise ValueError(msg_2)
