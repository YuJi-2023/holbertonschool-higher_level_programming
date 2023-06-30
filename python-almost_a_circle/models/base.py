#!/usr/bin/python3
"""define class Base"""
import json
import os


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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write json string of list_objs to a file"""
        file_name = cls.__name__ + '.json'
        with open(file_name, "w") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                myFile.write(cls.to_json_string([obj.to_dictionary() for
                             obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """return the list of json string representation"""
        if json_string is None or json_string == '':
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

    @classmethod
    def load_from_file(cls):
        """return a list of instancs"""
        instance_list = []
        file_name = f"{cls.__name__}.json"
        if os.path.exists(file_name) is True:
            with open(file_name, "r") as json_file:
                dict_list = cls.from_json_string(json_file.read())
            for item in dict_list:
                instance = cls.create(**item)
                instance_list.append(instance)
        return instance_list
