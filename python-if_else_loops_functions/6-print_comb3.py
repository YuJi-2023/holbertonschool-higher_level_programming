#!/usr/bin/python3
for first_digit in range(0, 10):
    for second_digit in range(0, 10):
        if first_digit < second_digit and first_digit != 8:
            print("{0}{1}, ".format(first_digit, second_digit), end="")
        elif first_digit < second_digit and first_digit == 8:
            print("{0}{1}".format(first_digit, second_digit))
