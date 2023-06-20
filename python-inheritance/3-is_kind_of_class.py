#!/usr/bin/python3
"""check for same class or subclass of"""


def is_kind_of_class(obj, a_class):
    """True if is an instance of a class or a subclass otherwise False."""
    if type(obj) is a_class or issubclass(type(obj), a_class):
        return True
    else:
        return False
