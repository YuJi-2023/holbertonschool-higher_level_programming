#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    divide_result_list = []
    index = 0
    for index in range(0, list_length):
        result = 0
        try:
            result = my_list_1[index] / my_list_2[index]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            divide_result_list.append(result)
    return divide_result_list
