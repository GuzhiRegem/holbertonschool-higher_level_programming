#!/usr/bin/python3
import sys
if __name__ == "__main__":
    out = 0
    args = sys.argv[1:]
    for arg in args:
        out += int(arg)
    print("{}".format(out))
