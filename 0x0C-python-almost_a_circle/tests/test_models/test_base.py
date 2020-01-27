#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import os
import unittest
from models.base import Base

class TestMaxInteger(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Setup """
        Base.__nb_objects = 0

    def test_empty_id(self):
        a0 = Base()
        self.assertEqual(a0.id, 1)

    def test_id(self):
        a0 = Base(89)
        self.assertEqual(a0.id, 89)
    
    def test_many_empty(self):
        a0 = Base()
        print(a0.id)
        a1 = Base()
        a2 = Base()
        self.assertEqual(a2.id, 4)
