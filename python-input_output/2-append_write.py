#!/usr/bin/python3
"""append a string to the end of a text file and return count"""


def append_write(filename="", text=""):
    """a function that append a string to a file and return count"""
    with open(filename, mode='a', encoding="utf-8") as myFile:
        myFile.write(text)
        nb_count = 0
        for c in text:
            nb_count += 1
        return nb_count
