#!/usr/bin/python3
"""
    nunca
    se
    sabe
"""


class Rectangle:
    """ morite """
    def __init__(self, width=0, height=0):
        """ iniciar """
        if type(width) != int:
            raise TypeError("width must be an integer")
            return
        if width < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = width
        if type(heigth) != int:
            raise TypeError("width must be an integer")
            return
        if width < 0:
            raise ValueError("width must be >= 0")
            return
        self.__width = width
