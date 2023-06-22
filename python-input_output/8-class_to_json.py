#!/usr/bin/python3
"""a function returns the dictionary description for JSON representation"""
import json


def class_to_json(obj):
    """json serialization for obj"""
    return obj.__dict__
