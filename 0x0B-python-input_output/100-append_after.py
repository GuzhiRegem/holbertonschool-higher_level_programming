#!/usr/bin/python3
"""
    100-append_after.py
    module
    return: nothing
"""


def append_after(filename="", search_string="", new_string=""):
    """ append after """
    fil = []
    with open(filename, "r") as f:
        for line in f:
            fil.append(line)
            if search_string in line:
                fil.append(new_string)
    with open(filename, "w") as f:
        for a in fil:
            f.write(a)
