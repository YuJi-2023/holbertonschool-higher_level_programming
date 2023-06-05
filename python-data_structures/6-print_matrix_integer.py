#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for idx_of_matrix in range(len(matrix)):
        list_in_matrix = matrix[idx_of_matrix]
        for idx_of_list in range(len(list_in_matrix)):
            if idx_of_list == 0:
                print("{:d}".format(list_in_matrix[idx_of_list]), end='')
            else:
                print(" {:d}".format(list_in_matrix[idx_of_list]), end='')
        print()
