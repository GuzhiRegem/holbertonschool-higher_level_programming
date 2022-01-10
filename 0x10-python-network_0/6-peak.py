#!/usr/bin/python3
"""
    6-peak.py
    module
    return: nothing
"""


def find_peak(list_of_integers):
    """ find peak """
    li = list_of_integers
    li1 = len(li)
    if li1 == 0:
        return
    m = li1 // 2
    if (m == li1 - 1 or li[m] >= li[m + 1]) and (m == 0 or li[m] >= li[m - 1]):
        return li[m]
    if m != li1 - 1 and li[m + 1] > li[m]:
        return find_peak(li[m + 1:])
    return find_peak(li[:m])
