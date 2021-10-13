#!/usr/bin/python3
"""
    1-write_file.py
    module
    return: nothing
"""


def write_file(filename="", text=""):
    """ write file """
    with open(filename, "w") as f:
        a = f.write(text)
        return a
