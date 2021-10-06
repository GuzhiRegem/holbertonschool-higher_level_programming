#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test1(self):
        """ muajajaja """
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test2(self):
        """ muajajaja """
        self.assertEqual(max_integer([3, 4, 3]), 4)

    def test3(self):
        """ muajajaja """
        self.assertEqual(max_integer([1, 0, 0]), 1)

    def test4(self):
        """ muajajaja """
        self.assertEqual(max_integer([]), None)

    def test6(self):
        """ muajajaja """
        self.assertEqual(max_integer([1, 2, -3]), 2)

    def test7(self):
        """ muajajaja """
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test8(self):
        """ muajajaja """
        self.assertEqual(max_integer([1]), 1)
