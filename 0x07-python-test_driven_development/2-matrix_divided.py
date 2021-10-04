#!/usr/bin/python3
"""
    this
    is
    DOCUMENTATION
"""


def matrix_divided(matrix, div):
    """ matrix but divided """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(msg)
        return
    if div == 0:
        raise ZeroDivisionError("division by zero")
        return
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
        return
    out = []
    for a in matrix:
        if not isinstance(a, list):
            raise TypeError(msg)
            return
        row = []
        leng = len(matrix[0])
        if len(a) != leng:
            raise TypeError("Each row of the matrix must have the same size")
        for b in a:
            if type(b) not in [int, float]:
                raise TypeError(msg)
                return
            row.append(round(b / div, 2))
        out.append(row)
    return out
