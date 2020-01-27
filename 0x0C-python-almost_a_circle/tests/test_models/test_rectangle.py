#!/usr/bin/python3
"""Unittest for Rectangle
"""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestMaxInteger(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Setup """
        Base.__nb_objects = 0

    def test_inheritance(self):
        self.assertTrue(issubclass(Rectangle, Base))

