#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
