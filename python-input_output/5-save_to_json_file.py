#!/usr/bin/python3
"""write an Object to a file using JSON string representation"""
import json


def save_to_json_file(my_obj, filename):
    """write JSON representation of an obj to a file"""
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(json.dumps(my_obj))
