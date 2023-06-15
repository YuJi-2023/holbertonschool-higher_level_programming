#!/usr/bin/python3
"""
This is the "print_square" module.
"""


def print_square(size):
    """
    Function to prints a square with the character #.

    Args:
        size: int >= 0

    Returns:
        print out the square to console
    """
    s1_msg = "size must be an integer"
    s2_msg = "size must be >= 0"
    m = "print_square() missing 1 required positional argument: 'size'"
    if not isinstance(size, int):
        raise TypeError(s1_msg)
    if size < 0:
        raise ValueError(s2_msg)
    for i in range(size):
        print('#' * size)
