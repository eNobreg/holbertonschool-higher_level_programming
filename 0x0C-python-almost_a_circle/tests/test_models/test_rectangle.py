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
        Base._Base__nb_objects = 0 

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

    def test_one(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, 0)

    def test_inf(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(float('inf'), float('inf'))

    def test_offsets(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "a", None)
            r2 = Rectangle(1, 1, 3, "b")
            r3 = Rectangle(1, 1, None, None)

    def test_zeroes(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 0, 0, 0)
        with self.assertRaises(ValueError):
            r2 = Rectangle(1, 0, 0, 0)
        with self.assertRaises(ValueError):
            r3 = Rectangle(0, 1, 0, 0)

    def test_offset_negatives(self):
        with self.assertRaises(ValueError):
                r1 = Rectangle(-1, -1, -1, -1)
        with self.assertRaises(ValueError):
                r2 = Rectangle(1, -1, -1, -1)
        with self.assertRaises(ValueError):
                r3 = Rectangle(1, 1, -1, -1) 
        with self.assertRaises(ValueError):
                r4 = Rectangle(1, 1, 1, -1)

    def test_stings(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("a", "a", "a", "a") 
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "a", "a", "a") 
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, "a", "a")
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, "a") 

    def test_empties(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(None, "a", "a", "a") 
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, None, "a", "a") 
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, None, "a") 
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1, 1, None)

    def test_str(self):
        r1 = Rectangle(1, 1)
        self.assertEqual(str(r1), "[Rectangle] (1) 0/0 - 1/1")

    def test_update(self):
        s1 = Rectangle(1, 1)
        s1.update(45, 1, 4, 4, 1)
        self.assertEqual(str(s1), "[Rectangle] (45) 4/1 - 1/4")

    def test_update_2(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        s1.update(1, 1, 4, 4, 4)
        self.assertEqual(str(s1), "[Rectangle] (1) 4/4 - 1/4")

    def test_update_3(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        s1.update(id="360")
        self.assertEqual(str(s1), "[Rectangle] (360) 1/1 - 1/1")
        
    def test_update_4(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        s1.update(id=500, wdith=400, height=500, x=5, y=5)
        self.assertEqual(str(s1), "[Rectangle] (500) 5/5 - 1/500")
        
    def test_update_5(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s1.update(id=500, width="500", height=400, x=5, y=5)
        
    def test_update_6(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        s1.update(1, 1, 1, 1, id=500, width=400, height=400, x=5, y=5)
        self.assertEqual(str(s1), "[Rectangle] (1) 1/1 - 1/1")

    def test_update_7(self):
        s1 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s1.update(width="hosue")
