#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    js = {
        "email":sys.argv[2]
    }
    r = requests.get(sys.argv[1], data=js)
    print(r.text)
