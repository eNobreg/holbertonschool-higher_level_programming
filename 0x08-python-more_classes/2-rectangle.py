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
        """ A docstring """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ A docstring """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ A docstring """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ A docstring """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__height = value

    def area(self):
        """ Area function """
        return(self.height * self.width)

    def perimeter(self):
        """ Perimeter function """
        if self.width == 0 or self.height == 0:
            return 0
        return (2*(self.width + self.height))
