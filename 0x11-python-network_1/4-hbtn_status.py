#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    t = r.text
    print("\t- type: {}".format(type(t)))
    print("\t- content: {}".format(t))
