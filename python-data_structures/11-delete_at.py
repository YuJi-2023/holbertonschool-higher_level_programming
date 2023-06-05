#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        idx_to_delete = idx
        del my_list[idx_to_delete]
        return my_list
