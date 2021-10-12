#!/usr/bin/python3
"""
	101-add_attribute.py
	module
	return: nothing
"""


def add_attribute(a_class, a_name, a_value):
    if hasattr(a_class, '__dict__'):
        setattr(a_class, a_name, a_value)
    else:
        raise TypeError("can't add new attribute")
