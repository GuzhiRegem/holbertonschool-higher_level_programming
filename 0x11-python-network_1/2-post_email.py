#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import urllib.request
import sys


if __name__ == "__main__":
    bdy = {
        "email": sys.argv[2]
    }
    with urllib.request.urlopen(sys.argv[1], bdy) as res:
        print(res.read().decode("utf-8"))
