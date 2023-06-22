#!/usr/bin/python3
"""return an object that represented by JSON string"""
import json


def from_json_string(my_str):
    """return an object from JSON"""
    return json.loads(my_str)
