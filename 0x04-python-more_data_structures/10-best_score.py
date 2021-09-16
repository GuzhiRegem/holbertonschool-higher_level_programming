#!/usr/bin/python3


def best_score(a_dictionary):
        out = None
        if len(a_dictionary) > 0:
                out = max(a_dictionary, key=a_dictionary.get)
        return out
