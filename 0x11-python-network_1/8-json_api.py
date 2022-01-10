#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    q = "" if len(sys.argv) <= 1 else sys.argv[1]
    data = {"q": q}
    r = requests.post(sys.argv[1], data=data)
    try:
        d = r.dict()
        if len(r) > 0:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
