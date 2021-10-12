#!/usr/bin/python3
"""
    4-inherits_from.py
    module
    return: nothing
"""


def inherits_from(obj, a_class):
    """ True if the object is an instance of a class that inherited """
    return issubclass(type(obj), a_class)
