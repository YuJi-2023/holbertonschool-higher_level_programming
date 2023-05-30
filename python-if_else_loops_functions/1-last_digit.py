#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str_1 = 'Last digit of'
str_2 = 'is'
if number >= 0:
    last_digit = number % 10
elif number < 0:
    last_digit = number % 10 - 10

if last_digit > 5:
    print(f"{str_1} {number} {str_2} {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{str_1} {number} {str_2} {last_digit} and is 0")
else:
    print(f"{str_1} {number} {str_2} {last_digit} \
and is less than 6 and not 0")
