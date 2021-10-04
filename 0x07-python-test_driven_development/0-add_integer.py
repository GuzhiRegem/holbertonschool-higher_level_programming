#!/usr/bin/python3
"""
    this is a module
    deamn
    return: algo
"""


def add_integer(a, b=98):
    """ cualquiera """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
        return
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
        return
    return int(a) + int(b)
