#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Tests for function """
    def test_empty(self):
        """ Tests for function """
        self.assertEqual(max_integer([]), None)
    def test_normal(self):
        """ Tests for function """
        self.assertEqual(max_integer([1, 2, 3 ,4]), 4)
    def test_max_in_second(self):
        """ Tests for function """
        self.assertEqual(max_integer([3, 78, 8, 2]), 78)
    def test_one(self):
        """ Tests for function """
        self.assertEqual(max_integer([675]), 675)
    def test_strings(self):
        """ Tests for function """
        self.assertEqual(max_integer(["alpha", "bravo"]), "bravo")
    def test_negatives(self):
        """ Tests for function """
        self.assertEqual(max_integer([-2, -5, -98, -103]), -2)
    def test_mixed_long(self):
        """ Tests for function """
        self.assertEqual(max_integer([-2, -5, -98, -103, 200, 5042, 1, 2, 5, 9, 90, 80]), 5042)
    def one_string(self):
        """ Tests for function """
        self.assertEqual(max_integer([":"]), ":")
    def two_strings(self):
        """ Tests for function """
        self.assertEqual(max_integer([":", "?"]), "?")
