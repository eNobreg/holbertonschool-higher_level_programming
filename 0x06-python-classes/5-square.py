#!/usr/bin/python3
""" File to define a square  """
class Square:
    """ A square of size """
    def __init__(self, size=0):
        """ Initialized Size  """
        self.size = size
    def area(self):
        """ Area of square """
        return(self.__size * self.__size)
    @property
    def size(self):
        return (self.__size)
    @size.setter
    def size(self, value):
        """ sets the size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value 
    def my_print(self):
        """ Print a square """
        for i in range(0, self.size):
            for j in range(self.size):
                print("#", end="")
            print()
        if (self.size is 0):
            print()
