#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for list_in_matrix in matrix:
        new_list = []
        for elem in list_in_matrix:
            new_list.append(elem ** 2)
        new_matrix.append(new_list)
    return new_matrix
