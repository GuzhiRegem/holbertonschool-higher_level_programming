#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    lar = len(my_list)
    if my_list:
        for idx in range(lar):
            print("{:d}".format(my_list[lar-(idx + 1)]))
    else:
        print("", end="")
