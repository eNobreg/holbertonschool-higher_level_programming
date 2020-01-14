#!/usr/bin/python3
""" Module for holberton project  """


class Rectangle:
    """ A class for doing things with a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __del__(self):
        print("Bye rectangle...")

    @property
    def width(self):
        return(self.__width)

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("value must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)

    @height.setter
    def height(self, value):
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

    def __str__(self):
        """ Str representation """
        new_str = ""
        if self.width == 0 or self.height == 0:
            return new_str
        for i in range(self.height):
            new_str += "#" * self.width
            new_str += '\n'
        return (new_str[:-1])

    def __repr__(self):
        """ Returns a representation """
        return ("Rectangle({}, {})".format(self.width, self.height))
