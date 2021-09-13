#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    out = []
    for ele in my_list:
        out.append(ele % 2 == 1)
    return out
