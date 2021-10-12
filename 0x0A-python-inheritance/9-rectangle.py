#!/usr/bin/python3
"""
    7-base_geometry.py
    module
    return: nothing
"""


class BaseGeometry:
    """ BaseGeometry """
    def area(self):
        """ area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")

class Rectangle(BaseGeometry):
    """ Rectangle """
    def __init__(self, width, height):
        """ init """
        try:
            super().integer_validator("width", width)
            self.__width = width
        except Exception as e:
            raise e
        try:
            super().integer_validator("height", height)
            self.__height = height
        except Exception as e:
            raise e

    def area(self):
        """ area """
        return self.__width * self.__height

    def __str__(self):
        """ str """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
