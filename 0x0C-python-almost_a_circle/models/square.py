#!/usr/bin/python3
"""
    square.py
    module
    return: nothing
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ init """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size """
        return self.width

    @size.setter
    def size(self, value):
        """ size """
        self.width = value
        self.height = value

    def __str__(self):
        """ str """
        st1 = "{}/{}".format(self.x, self.y)
        st2 = self.width
        return "[Square] ({}) {} - {}".format(self.id, st1, st2)

    def update(self, *args, **kwargs):
        """ update """
        le = len(args)
        if le >= 1:
            self.id = args[0]
        if le >= 2:
            self.width = args[1]
            self.height = args[1]
        if le >= 3:
            self.x = args[2]
        if le >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ to dict """
        out = {}
        out['id'] = self.id
        out['size'] = self.width
        out['x'] = self.x
        out['y'] = self.y
        return out
