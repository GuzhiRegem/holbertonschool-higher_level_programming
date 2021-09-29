#!/usr/bin/python3
"""
    3-square.py
    life is to suffer
    return {}
"""


class Square:
    """
        square
    """
    def __init__(self, size=0):
        """ init """
        if type(size) != int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """ area """
        return self.__size ** 2
