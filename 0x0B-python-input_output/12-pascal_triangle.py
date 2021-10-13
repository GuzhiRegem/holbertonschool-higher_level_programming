#!/usr/bin/python3
"""
    12-pascal_triangle.py
    module
    return: nothing
"""


def pascal_triangle(n):
    """ pascal """
    lis = [[1]]
    if n <= 0:
        return []
    for i in range(n - 1):
        tmp = [0] * (len(lis[-1]) + 1)
        for num in range(len(lis[-1])):
            tmp[num] += lis[-1][num]
            tmp[num + 1] += lis[-1][num]
        lis.append(tmp)
    return lis
