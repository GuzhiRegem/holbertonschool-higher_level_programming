#!/usr/bin/python3
"""
    7-add_item.py
    module
    return: nothing
"""
import json
import sys


load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file


lis = list(sys.argv)[1:]
try:
    lis1 = load_from_json_file("add_item.json")
    for a in lis1:
        lis.insert(0, a)
except Exception as e:
    pass
save_to_json_file(lis, "add_item.json")
