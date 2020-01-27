#!/usr/bin/python3
"""Unittest for Rectangle
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class r_t(unittest.TestCase):
    """ Test Cases """
    r1 = Rectangle(5, 5)
    r2 = Rectangle(3, 3)
    r3 = Rectangle(9, 9)

    def setUp(self):
        """ Setup """
        r3 = Rectangle(9, 9)

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

    def test_area(self):
        """ tests """
        r1 = Rectangle(5, 5)
        r2 = Rectangle(3, 3)
        r3 = Rectangle(9, 9)
        self.assertEqual(r1.area(), 25)
        self.assertEqual(r2.area(), 9)
        self.assertEqual(r3.area(), 81)

    def test_negatives(self):
        """ Nagative """
        with self.assertRaises(ValueError):
            r1 = Rectangle(-5, -4)

    def test_none(self):
        """ Testing none input """
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, None)
    
    def test_equal_dicts(self):
        r1 = Rectangle(1, 2, 3, 4)
        diction = r1.to_dictionary()
        self.assertEqual(r1.to_dictionary(), diction)


