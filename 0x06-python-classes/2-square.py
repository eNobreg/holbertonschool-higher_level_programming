#!/usr/bin/python3
""" File to define a square  """
class Square:
    """ A square of size """
    def __init__(self, size=0):
        """ Initialized Size  """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif(size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
