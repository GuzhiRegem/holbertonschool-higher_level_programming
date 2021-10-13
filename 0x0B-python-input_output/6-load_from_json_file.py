#!/usr/bin/python3
"""
    6-load_from_json_file.py
    module
    return: nothing
"""
import json


def load_from_json_file(filename):
    """ load to json """
    with open(filename, "r") as f:
        return json.loads(f.read())
