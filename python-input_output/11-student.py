#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """instantiate with three attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of attrs in the list"""
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """replace all attrs of the class"""
        self.__dict__ = json
