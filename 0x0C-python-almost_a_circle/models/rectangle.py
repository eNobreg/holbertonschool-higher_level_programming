#!/usr/bin/python3
""" Module file """

from models.base import Base
class Rectangle(Base):
    """ Recetangle Class for Almost a circle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Init """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def x(self):
        """ Getter for X"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ X setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ y getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def area(self):
        """ Area of rectangle """
        return (self.width * self.height)

    def display(self):
        """ Displays Rectangle """
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end='')
            print("#" * self.width)

    def __str__(self):
        """ Override str method """
        h = ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, 
                                                     self.width, self.height))
        return h

    def update(self, *args, **kwargs): 
        """ Update Arguments """
        if len(args) > 0:
            try: 
                super().__init__(args[0])
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
            except:
                pass
        else: 
            super().__init__(kwargs.get('id', self.id))
            self.height = kwargs.get('height', self.height)
            self.width = kwargs.get('width', self.width)
            self.x = kwargs.get('x', self.x)
            self.y = kwargs.get('y', self.y)

    def to_dictionary(self):
        """ To dictionary """
        new = {}
        atts = ["id", "height", "width", "x", "y"]
        for k, v in self.__dict__.items():
            key = k.partition('__')
            if key[2] in atts:
                new[key[2]] = v
            if k in atts:
                new[k] = v
        return new
