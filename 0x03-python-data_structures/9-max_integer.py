#!/usr/bin/python3


def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxi = my_list[0]
    for inte in my_list:
        if inte > maxi:
            maxi = inte
    return maxi
