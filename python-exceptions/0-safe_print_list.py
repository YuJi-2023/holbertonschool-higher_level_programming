#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for elem in my_list[:x]:
            print(elem, end='')
        print()
    except IndexError:
        pass
    j = 0
    for i in my_list:
        j = j + 1
    if x < j:
        return x
    else:
        return j
