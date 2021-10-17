#!/usr/bin/python3
"""
    testing
    module
    return: nothing
"""
import unittest
from models.base import Base


class TestEx1(unittest.TestCase):
    """ excercise 1 tester """

    def testCase1(self):
        """ Test case 1 """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testCase2(self):
        """ Test case 2 """
        b1 = Base(34)
        self.assertEqual(b1.id, 34)

    def testCase3(self):
        """ Test case 3 """
        b1 = Base()
        self.assertEqual(b1.id, 2)


class TestEx1(unittest.TestCase):
    """ excercise 1 tester """

    def testCase1(self):
        """ Test case 1 """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def testCase2(self):
        """ Test case 2 """
        b1 = Base(34)
        self.assertEqual(b1.id, 34)

    def testCase3(self):
        """ Test case 3 """
        b1 = Base()
        self.assertEqual(b1.id, 2)
