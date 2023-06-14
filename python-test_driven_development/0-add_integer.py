#!/usr/bin/python3
"""
This is the "add_integer" module.

The add_integer module has one function, add_integer().
"""


def add_integer(a, b=98):
    """
    Function to add two integers.

    Args:
        a (int or float): The first number.
        b (int or float): The second number, with a default value of 98.

    Returns:
        int: The sum of the two numbers.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
