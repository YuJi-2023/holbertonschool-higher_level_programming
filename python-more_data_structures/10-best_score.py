#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        sorted_keys = sorted(a_dictionary, key=a_dictionary.get)
        return sorted_keys[-1]
    else:
        return None
