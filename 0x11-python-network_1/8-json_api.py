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
    r = requests.post("http://0.0.0.0:5000/search_user", {"q": q})
    try:
        d = r.dict()
        if r:
            print("[{}] {}".format(r.get("id"), r.get("name")))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
