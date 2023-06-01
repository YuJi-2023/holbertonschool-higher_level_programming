#!/usr/bin/python3
import sys


def show_argv():
    count = len(sys.argv) - 1
    if count == 1:
        print(f"{count} argument:")
        print(f"1: {sys.argv[1]}")
    elif count > 1:
        print(f"{count} arguments:")
        for i in range(1, count + 1):
            print(f"{i}: {sys.argv[i]}")
    else:
        print(f"{count} arguments.")


if __name__ == "__main__":
    show_argv()
