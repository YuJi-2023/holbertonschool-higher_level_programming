#!/usr/bin/python3
def print_last_digit(number):
    number_to_str = str(number)
    last_digit = number_to_str[-1]
    print(f"{last_digit}", end='')
    return int(last_digit)
