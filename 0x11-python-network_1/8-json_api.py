#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    data = {"q":""}
    if len(sys.argv) > 1:
        data["q"] = sys.argv[1]
    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        d = r.json()
        if "id" not in d or "name" not in d:
            print("No result")
        else:
            print("[{}] {}".format(r.get("id"), r.get("name")))
    except ValueError:
        print("Not a valid JSON")
