#!/usr/bin/python3


def search_replace(my_list, search, replace):
        out = my_list[:]
        for i, a in enumerate(out):
                if a == search:
                        out[i] = replace
        return out
