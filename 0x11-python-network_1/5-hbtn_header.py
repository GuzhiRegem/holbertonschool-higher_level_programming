#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    h = r.headers
    print(h.get("X-Request-Id"))
