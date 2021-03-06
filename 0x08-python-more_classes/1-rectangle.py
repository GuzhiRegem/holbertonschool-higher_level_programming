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
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ alol """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ jajajajaja """
        return self.__height

    @height.setter
    def height(self, value):
        """ matenme """
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
