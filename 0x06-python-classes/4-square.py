#!/usr/bin/python3
"""
    4-square
    que alguien me mate
    return {}
"""


class Square:
    """
        square
    """
    def __init__(self, size=0):
        """ init """
        self.__size = size
    def area(self):
        """ area """
        return self.__size ** 2
    @property
    def size(self):
        """ size """
        return self.__size

    @size.setter
    def size(self, value):
        """ size """
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
