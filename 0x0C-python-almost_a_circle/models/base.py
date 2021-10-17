#!/usr/bin/python3
"""
    base.py
    module
    return: nothing
"""
import json


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ to json """
        if list_dictionaries is None:
            return "[]"
        if len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to file """
        lis = []
        for a in list_objs:
            lis.append(a.to_dictionary())
        st = cls.to_json_string(lis)
        filename = str(cls.__name__) + ".json"
        with open(filename, "w") as f:
            f.write(st)

    @staticmethod
    def from_json_string(json_string):
        """ from json """
        if json_string is None:
            return []
        if json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ create """
        dum = cls(1,1)
        dum.update(**dictionary)
        return dum

    @classmethod
    def load_from_file(cls):
        """ load from file """
        filen = str(cls.__name__) + ".json"
        try:
            with open(filen, "r") as f:
                li = json.loads(f.read())
                out = []
                for a in li:
                    out.append(cls.create(**a))
                return out
        except FileNotFoundError:
            return []
