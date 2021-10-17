#!/usr/bin/python3
"""
    rectangle.py
    module
    return: nothing
"""
from models.base import Base


class Rectangle(Base):
    """ rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init """
        super().__init__(id)
        if self.validate("width", width, 1):
            self.__width = width
        if self.validate("height", height, 1):
            self.__height = height
        if self.validate("x", x, 0):
            self.__x = x
        if self.validate("y", y, 0):
            self.__y = y

    def validate(self, name, value, num):
        """ validator """
        if type(value) != int:
            raise TypeError(name + " must be an integer")
            return False
        if value < num:
            sig = (">" if value == 1 else ">=")
            raise ValueError("{} must be {} 0".format(name, sig))
            return True
                
                
        return True

    @property
    def width(self):
        """ width """
        return self.__width

    @width.setter
    def width(self, value):
        """ width """
        if self.validate("width", value, 1):
            self.__width = value

    @property
    def height(self):
        """ height """
        return self.__height

    @height.setter
    def height(self, value):
        """ height """
        if self.validate("height", value, 1):
            self.__height = value

    @property
    def x(self):
        """ x """
        return self.__x

    @x.setter
    def x(self, value):
        """ x """
        if self.validate("x", value, 0):
            self.__x = value

    @property
    def y(self):
        """ y """
        return self.__y

    @y.setter
    def y(self, value):
        """ y """
        if self.validate("y", value, 0):
            self.__y = value
