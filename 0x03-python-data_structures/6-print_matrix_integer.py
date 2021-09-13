#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for y in matrix:
        indx = 0
        for x in y:
            print("{}{}".format(" " if indx else "", x), end="")
            indx += 1
        print()
