#!/usr/bin/python3
""" Method """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle Class """
    def __init__(self, width, height):
        """ Instantiation method for rectangle class"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ I want it to work"""
        i = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return(i)

    def area(self):
        """ I want to understand """
        return self.__height * self.__width
