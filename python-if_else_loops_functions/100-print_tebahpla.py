#!/usr/bin/python3
for value in range(90, 64, -1):
    if value % 2 == 0:
        value = value + 32
    print(f"{chr(value)}", end='')
