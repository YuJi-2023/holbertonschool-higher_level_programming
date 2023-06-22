#!/usr/bin/python3
"""write a string to a text file and return count of chars written"""


def write_file(filename="", text=""):
    """a function that write to a file and return count"""
    with open(filename, mode='w', encoding="utf-8") as myFile:
        myFile.write(text)
        nb_count = 0
        for c in text:
            nb_count += 1
        return nb_count
