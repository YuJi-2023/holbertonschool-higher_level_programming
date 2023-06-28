#!/usr/bin/python3
"""define class Base"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """return JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string of list_objs to a file"""
        file_name = cls.__name__ + '.json'
        if list_objs is None:
            list_objs = []
        json_str = cls.to_json_string(obj.to_dictionary() for obj in list_objs)
        with open(file_name, 'w') as myFile:
            myFile.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """return the list of json string representation"""
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set"""
        if dictionary != {}:
            if cls.__name__ == 'Rectangle':
                instance = cls(2, 3)
            else:
                instance = cls(2)
        instance.update(**dictionary)
        return instance
