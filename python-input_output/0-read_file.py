#!/usr/bin/python3
"""read a text file and print to stdout"""


def read_file(filename=""):
    """a function that read a file with open"""
    with open(filename, encoding="utf-8") as myFile:
        print(myFile.read(), end='')
