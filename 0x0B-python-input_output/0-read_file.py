#!/usr/bin/python3
"""
    0-read_file.py
    module
    return: nothing
"""


def read_file(filename=""):
    """ read file """
    with open(filename, "r") as f:
        for i in list(f):
            print(i, end="")
