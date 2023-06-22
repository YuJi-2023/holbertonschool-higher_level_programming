#!/usr/bin/python3
"""add to list and save to JSON file"""
import os
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""add obj to JSON file and load from it after"""
filename = "add_item.json"
if not os.path.exists(filename):
    my_list = []
else:
    my_list = load_from_json_file(filename)

my_list.extend(sys.argv[1:])
save_to_json_file(my_list, filename)
