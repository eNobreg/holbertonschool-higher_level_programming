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
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

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
        self.assertEqual(max_integer([-5, -98, -1, 2, 5042, 9, 90, 80]), 5042)

    def one_string(self):
        """ Tests for function """
        self.assertEqual(max_integer([":"]), ":")

    def two_strings(self):
        """ Tests for function """
        self.assertEqual(max_integer([":", "?"]), "?")

    def test_duplicates(self):
        """ This Function  """
        self.assertEqual(max_integer([1, 1]), 1)

    def test_zeroes(self):
        """ Function to test zeroes  """
        self.assertEqual(max_integer([0, 0]), 0)

    def test_strings(self):
        """ This function """
        self.assertEqual(max_integer("string"), 't')

    def test_none(self):
        """ This function """
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_tuple(self):
        """ Test Tuple """
        self.assertEqual(max_integer((3.7, 4.8)), 4.8)

    def test_blank_tuple(self):
        """ Tuple Testing  """
        self.assertEqual(max_integer(()), None)
