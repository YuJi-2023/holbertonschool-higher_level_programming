#!/usr/bin/python3
"""check for subclass only"""


def inherits_from(obj, a_class):
    """True if is of subclass otherwise False."""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
