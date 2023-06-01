#!/usr/bin/python3
import hidden_4


def hidden_discovery():
    name_list = dir(hidden_4)
    index = 0
    for index in range(0, len(name_list)):
        if name_list[index][0:2] != '__':
            print(f"{name_list[index]}")


if __name__ == "__main__":
    hidden_discovery()
