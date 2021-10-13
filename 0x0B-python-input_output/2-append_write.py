#!/usr/bin/python3
"""
    2-append_write.py
    module
    return: nothing
"""


def append_write(filename="", text=""):
    """ append write """
    with open(filename, "a") as f:
        return f.write(text)
