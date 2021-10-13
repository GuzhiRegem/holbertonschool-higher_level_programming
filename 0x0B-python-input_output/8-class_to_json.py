#!/usr/bin/python3
"""
    8-class_to_json.py
    module
    return: nothing
"""
import json


def class_to_json(obj):
    """ class to json """
    return json.dumps(obj.__dict__)
