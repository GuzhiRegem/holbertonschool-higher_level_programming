#!/usr/bin/python3


def multiply_by_2(a_dictionary):
        b_dictionary = dict(a_dictionary)
        for i in b_dictionary.items():
                b_dictionary[i[0]] = i[1] * 2
        return b_dictionary
