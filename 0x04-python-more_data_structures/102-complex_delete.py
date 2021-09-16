#!/usr/bin/python3
def complex_delete(a_dictionary, value):
        rm = []
        for i in a_dictionary.items():
                if i[1] == value:
                        rm.append(i[0])
        for i in rm:
                del a_dictionary[i]
        return a_dictionary
