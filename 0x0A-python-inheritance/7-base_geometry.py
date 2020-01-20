#!/usr/bin/python3
""" Module for class """


class BaseGeometry:
    """ Bse Geometry class"""

    def area(self):
        """ Area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validate given ints"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")
