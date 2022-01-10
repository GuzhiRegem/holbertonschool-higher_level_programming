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

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
