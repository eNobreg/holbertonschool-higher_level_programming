#!/usr/bin/python3
""" File to define a square  """


class Square:
    """ A square of size """
    def __init__(self, size=0, position=(0, 0)):
        """ Initialized Size  """
        self.size = size
        self.position = position

    def area(self):
        """ Area of square """
        return(self.size * self.size)

    @property
    def size(self):
        """ First getter function """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ sets the size """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Position to print """
        return self.__position

    @position.setter
    def position(self, value):
        """ Checks positions  """
        if (len(value) is not 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (type(value[0]) is not int or value[0] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(type(value[1]) is not int or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ Print a square """
        if (self.size == 0):
            print()
        else:
            for y in range(self.position[1]):
                print()
            for i in range(0, self.size):
                for e in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()
