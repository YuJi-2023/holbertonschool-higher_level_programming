#!/usr/bin/python3
def roman_to_int(roman_string):
    number_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':
                  1000}
    number = 0
    last_digit = 0
    if roman_string is None or type(roman_string) != str:
        return 0
    else:
        for roman_digit in roman_string[::-1]:
            roman_digit_value = number_map[roman_digit]
            if roman_digit_value >= last_digit:
                number += roman_digit_value
                last_digit = roman_digit_value
            else:
                number -= roman_digit_value
        return number
