#!/usr/bin/python3
"""
This is the "matrix_divided" module.
"""


def say_my_name(first_name, last_name=""):
    """
    Function to prints My name is <first name> <last name>.

    Args:
        first_name: a string
        last_name: a string, default ""

    Returns:
        formatted string and print out to console
    """
    f_msg = "first_name must be a string"
    l_msg = "last_name must be a string"
    m = "say_my_name() missing 1 required positional argument: 'first_name'"
    if not isinstance(first_name, str):
        raise TypeError(f_msg)
    if not isinstance(last_name, str):
        raise TypeError(l_msg)
    if not first_name:
        raise TypeError(m)
    print(f"My name is {first_name} {last_name}")
