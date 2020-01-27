#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestMaxInteger(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Setup """
        Base._Base__nb_objects = 0

    def test_id_types(self):
        """ Unit test """
        a0 = Base("a")
        self.assertEqual(a0.id, 'a')

    def test_empty_id(self):
        """ Unit test """
        a0 = Base()
        self.assertEqual(a0.id, 1)

    def test_nagative_id(self):
        """ Unit Test """
        a0 = Base(-1)
        self.assertEqual(a0.id, -1)

    def test_id(self):
        """ Unit test """
        a0 = Base(89)
        self.assertEqual(a0.id, 89)
    
    def test_many_empty(self):
        """ Unit test """
        a0 = Base()
        a1 = Base()
        a2 = Base()
        self.assertEqual(a2.id, 3)

    def test_none_id(self):
        a0 = Base(None)
        self.assertEqual(a0.id, 1)

    def test_to_inf(self):
        a0 = Base(float('inf'))
        self.assertEqual(a0.id, float('inf'))

    def test_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)
