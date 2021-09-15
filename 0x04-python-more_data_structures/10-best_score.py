#!/usr/bin/python3


def best_score(a_dictionary):
        out = list(a_dictionary.items())[0][1]
        key = ""
        for i in a_dictionary.items():
                if i[1] > out:
                        out = i[1]
                        key = i[0]
        return key
