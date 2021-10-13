#!/usr/bin/python3
"""
    10-student.py
    module
    return: nothing
"""


class Student:
    """ student """
    def __init__(self, first_name, last_name, age):
        """ init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        if type(attrs) == list:
            dic = {}
            for a, b in self.__dict__.items():
                if a in attrs:
                    dic[a] = b
            return str(dic)
        else:
            return str(self.__dict__)
