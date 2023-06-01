#!/usr/bin/python3
import sys


def add_all():
    count = len(sys.argv) - 1
    if count == 0:
        print(f"{count}")
    else:
        result = 0
        for i in range(0, count):
            result += int(sys.argv[i + 1])
        print(f"{result}")


if __name__ == "__main__":
    add_all()
