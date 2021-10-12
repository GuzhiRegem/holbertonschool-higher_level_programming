#!/usr/bin/python3
"""
	100-my_int.py
	module
	return: nothing
"""


class MyInt(int):
    """ MyInt """
    def __eq__(self, other):
        return self.real != other.real

    def __ne__(self, other):
        return self.real == other.real
