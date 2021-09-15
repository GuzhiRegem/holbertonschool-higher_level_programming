#!/usr/bin/python3


def multiply_by_2(a_dictionary):
        out = a_dictionary[0]
        for i in a_dictionary.items():
                if i[1] > out:
                        out = i[1]
        return out
