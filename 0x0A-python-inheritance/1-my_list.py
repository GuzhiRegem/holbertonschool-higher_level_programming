#!/usr/bin/python3
"""
    1-my_list.py
    module
    return: nothing
"""

class MyList(list):
    """ my list """
    def print_sorted(self):
        print(sorted(self))

