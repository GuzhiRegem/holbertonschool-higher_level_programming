#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    lar = len(my_list)
    if lar == 0:
        print("{}".format("\n"), end="")
    for idx in range(lar):
        print("{:d}".format(my_list[-(idx + 1)]))
