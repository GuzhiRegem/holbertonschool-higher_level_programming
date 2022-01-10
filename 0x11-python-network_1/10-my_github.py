#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    a = (sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", verify=False, auth=a)
    if "id" in r.json():
        print(r.json().get("id"))
    else:
        print("None")
