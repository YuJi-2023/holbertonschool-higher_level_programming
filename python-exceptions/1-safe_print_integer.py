#!/usr/bin/python3
def safe_print_integer(value):
    if type(value) is int:
        print("{:d}".format(value))
        return True
    else:
        return False
