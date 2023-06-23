#!/usr/bin/python3
"""Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """instantiate with three attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dict representation"""
        return self.__dict__
