#!/usr/bin/python3
import sys
def safe_function(fct, *args):
    out = None
    try:
        out = fct(*args)
    except Exception as exe:
        sys.stderr.write("Exception: {}\n".format(str(exe)))
    return out
