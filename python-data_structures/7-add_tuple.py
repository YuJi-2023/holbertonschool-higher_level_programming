#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    zero_tuple = (0, 0)
    tuple_a = tuple_a + zero_tuple
    tuple_b = tuple_b + zero_tuple
    first_add = tuple_a[0] + tuple_b[0]
    second_add = tuple_a[1] + tuple_b[1]
    new_tuple = (first_add, second_add)
    return (new_tuple)
