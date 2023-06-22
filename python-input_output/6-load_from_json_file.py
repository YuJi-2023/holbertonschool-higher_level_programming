#!/usr/bin/python3
"""creat an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """create an obj from JSON representation"""
    with open(filename, encoding="utf-8") as myObj:
        str_rep = myObj.readlines()
        for line in str_rep:
            return json.loads(line)
