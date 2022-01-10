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
    cod = r.status_code
    print(r.text if cod < 400 else "Error code: {}".format(cod))
