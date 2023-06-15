#!/usr/bin/python3
"""
This is the "matrix_divided" module.
"""


def matrix_divided(matrix, div):
    """
    Function to divides all elements of a matrix.

    Args:
        matrix: a list of lists of integers or floats
        div: a number (integer or float) not 0

    Returns:
        new matrix: result rounded to 2 decimal places
    """
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"
    new_matrix = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not all(map(lambda row: len(row) == len(matrix[0]), matrix[1:])):
        raise TypeError("Each row of the matrix must have the same size")
    for list_in_matrix in matrix:
        new_list = []
        for elem in list_in_matrix:
            if not isinstance(elem, (int, float)):
                raise TypeError(matrix_msg)
            else:
                new_list.append(float("{:.2f}".format(elem / div)))
        new_matrix.append(new_list)
    return new_matrix
