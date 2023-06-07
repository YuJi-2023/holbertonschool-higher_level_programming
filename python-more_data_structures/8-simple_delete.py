#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    keys_list = a_dictionary.keys()
    if key in keys_list:
        del a_dictionary[key]
    return a_dictionary
