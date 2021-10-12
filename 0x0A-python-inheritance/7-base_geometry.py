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
