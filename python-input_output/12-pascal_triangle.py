#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """function return a list representation of a pascal triangle for print"""
    pascal_list = []

    for i in range(0, n):
        row = [1]
        for j in range(1, i):
            next_elem = pascal_list[i - 1][j - 1] + pascal_list[i - 1][j]
            row.append(next_elem)
        if i > 0:
            row.append(1)
        pascal_list.append(row)
    return pascal_list
