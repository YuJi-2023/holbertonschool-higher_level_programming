#!/usr/bin/python3
"""define class Base"""


class Base:
    """set class attribute"""
    __nb_objects = 0
    """instantialise data"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
