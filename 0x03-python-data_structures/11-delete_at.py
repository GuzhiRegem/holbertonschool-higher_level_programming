#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    back = my_list[:idx]
    front = my_list[idx + 1:]
    new_list = back + front
    for idx in range(len(new_list)):
        my_list[idx] = new_list[idx]
    del my_list[-1]
    return my_list
