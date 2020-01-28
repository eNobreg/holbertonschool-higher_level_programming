#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import os
import json
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):
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

    def test_none(self):
        a0 = Base(None)
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

    def test_mixed_calls(self):
        a0 = Base()
        del a0
        a1 = Base()
        self.assertEqual(a2.id, 2)

    def test_mixed_calls(self):
        a0 = Base()
        a1 = Base(40)
        a2 = Base()
        self.assertEqual(a2.id, 2)

    def test_private(self):
        a0 = Base()
        self.assertTrue('_Base__nb_objects' in Base.__dict__)

class Test_base_json(unittest.TestCase):
    """ Test Cases """

    def setUp(self):
        """ Setup """
        self.a0 = Base()
        self.list = [{'id': 10, "age": 21}, {"name": 'Bob', "id": 12}]
        Base._Base__nb_objects = 0

    def tearDown(self):
        del self.a0


    """ Json Tests """

    def test_json(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertIsInstance(json_dictionary, str)

    def test_normal(self):
        self.assertEqual(self.a0.to_json_string(self.list), json.dumps(self.list))

    def test_not_dict(self):
        self.assertEqual(self.a0.to_json_string(100), '100')

    def test_empty_dict(self):
        self.assertEqual(self.a0.to_json_string([{}, {}]), '[{}, {}]')

    def test_empty_list(self):
        self.assertEqual(self.a0.to_json_string([]), '[]')

    def test_no_arg(self):
        with self.assertRaises(TypeError):
            self.a0.to_json_string()

class test_files_json(unittest.TestCase):
    """ Test Cases for files """

    def setUp(self):
        self.a0 = Rectangle(5, 5, 0, 0)
        self.a1 = Rectangle(3, 3)
        self.a2 = Square(4)
        self.a3 = Square(6, 1, 1)

    def test_save(self):
        Square.save_to_file([self.a1, self.a0])
        self.assertTrue(os.path.exists('Square.json'))


    def test_rec_save(self):
        Rectangle.save_to_file([self.a1, self.a0])
        self.assertTrue(os.path.exists('Rectangle.json'))

