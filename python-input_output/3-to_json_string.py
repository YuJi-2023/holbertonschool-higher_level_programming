#!/usr/bin/python3
"""return JSON representation string"""
import json


def to_json_string(my_obj):
    """return the JSON representation of an object"""
    return json.dumps(my_obj)
