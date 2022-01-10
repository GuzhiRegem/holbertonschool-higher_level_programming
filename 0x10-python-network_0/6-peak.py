#!/usr/bin/python3
"""
    6-peak.py
    module
    return: nothing
"""

def find_peak(list_of_integers):
    """ find peak """
    out = None
    for idx, val in enumerate(list_of_integers[1:-1]):
        ind = idx + 1
        if list_of_integers[ind - 1] > val:
            continue
        if list_of_integers[ind + 1] > val:
            continue
        if type(out) == int:
            if out < val:
                out = val
        else:
            out = val
    return out
