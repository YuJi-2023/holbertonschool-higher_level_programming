#!/usr/bin/python3
"""Module that multiplies 2 matrices
"""


def matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices
        result has number of rows of m_a and columns of m_b
    """
    err_msg_1 = 'm_a must be a list'
    err_msg_2 = 'm_b must be a list'
    err_msg_3 = 'm_a must be a list of lists'
    err_msg_4 = 'm_b must be a list of lists'
    err_msg_5 = "m_a can't be empty"
    err_msg_6 = "m_b can't be empty"
    err_msg_7 = 'm_a should contain only integers or floats'
    err_msg_8 = 'm_b should contain only integers or floats'
    err_msg_9 = 'each row of m_a must be of the same size'
    err_msg_10 = 'each row of m_b must be of the same size'
    err_msg_11 = "m_a and m_b can't be multiplied"

    result_matrix = []

    if m_a == [] or m_a == [[]]:
        raise ValueError(err_msg_5)
    if m_b == [] or m_b == [[]]:
        raise ValueError(err_msg_6)
    if not isinstance(m_a, list):
        raise TypeError(err_msg_1)
    for elem in m_a:
        if not isinstance(elem, list):
            raise TypeError(err_msg_3)
        else:
            for value in elem:
                if not isinstance(value, (int, float)):
                    raise TypeError(err_msg_7)
    if not isinstance(m_b, list):
        raise TypeError(err_msg_2)
    for elem in m_b:
        if not isinstance(elem, list):
            raise TypeError(err_msg_4)
        else:
            for value in elem:
                if not isinstance(value, (int, float)):
                    raise TypeError(err_msg_8)
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError(err_msg_9)
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError(err_msg_10)
    if len(m_a[0]) != len(m_b):
        raise ValueError(err_msg_11)
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            row.append(sum)
        result_matrix.append(row)
    return result_matrix
