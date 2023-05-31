#!/usr/bin/python3
def uppercase(mystr):
    new_str = ""
    for c in mystr:
        if ord(c) in range(97, 123):
            new_str = new_str + chr(ord(c) - 32)
        else:
            new_str = new_str + c
    print(new_str)
