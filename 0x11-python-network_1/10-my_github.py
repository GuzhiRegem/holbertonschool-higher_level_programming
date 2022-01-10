#!/usr/bin/python3
"""
    0-hbtn_status.py
    module
    return: nothing
"""
import requests
import sys


if __name__ == "__main__":
    requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)
    r = requests.get("https://api.github.com/user", verify=False, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    if "id" in r.json():
        print(r.json().get("id"))
    else:
        print("None")
