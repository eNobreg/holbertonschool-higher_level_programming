#!/usr/bin/python3
""" Module for holberton project  """


class Rectangle:
    """ A class for doing things with a rectangle"""
    def __init__(self, width=0, height=0):
        """ A docstring """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ Getter for width property """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ Setter for width property """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height property """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ Setter for height property"""
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value
