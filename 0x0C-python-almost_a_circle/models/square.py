#!/usr/bin/python3
""" Module for a square """

from models.base import Base
from models.rectangle import Rectangle
class Square(Rectangle):
    """ Square """
    def __init__(self, size, x=0, y=0, id=None):
        """ This and That """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """ Getter for size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sizes """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
        """ Update the Square """
        if  len(args) > 0:
            try:
                self.id = args[0] 
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except:
                pass
        else:
           self.id = kwargs.get('id', self.id)
           self.size = kwargs.get('size', self.size)
           self.x = kwargs.get('x', self.x)
           self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """ To dictionary """
        new = {}
        atts = ["id", "size", "x", "y"]
        for k, v in self.__dict__.items():
            key = k.partition('__')
            if key[2] in atts:
                new[key[2]] = v
            if k in atts:
                new[k] = v
        return new
