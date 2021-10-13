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
out = []
try:
    out = list(load_from_json_file("add_item.json"))
except Exception as e:
    pass
out = out + lis
save_to_json_file(out, "add_item.json")
