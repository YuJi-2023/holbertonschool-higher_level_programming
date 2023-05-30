#!/usr/bin/python3
for ascii_value in range(97, 123):
    if ascii_value != 101 and ascii_value != 112:
        print("{0}".format(chr(ascii_value)), end="")
