#!/usr/bin/python3
"""
    8-class_to_json.py
    module
    return: nothing
"""


def class_to_json(obj):
    """ class to json """
    return dict(obj.__dict__)
