#!/usr/bin/python3
"""
    may
    doc
    ument
"""


def print_square(size):
    """ mauaajajaja """
    if type(size) != int:
        raise TypeError("size must be an integer")
        return
    if size < 0:
        raise ValueError("size must be >= 0")
        return
    for a in range(size):
        for b in range(size):
            print("#", end="")
        if (a + 1) < size:
            print()
