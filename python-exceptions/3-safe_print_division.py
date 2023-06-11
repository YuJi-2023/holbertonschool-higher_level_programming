#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divide_result = a / b
    except ZeroDivisionError:
        divide_result = None
    finally:
        print("Inside result: {}".format(divide_result))
        return divide_result
