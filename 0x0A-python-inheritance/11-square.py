#!/usr/bin/python3
""" Import under this """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ This """
    def __init__(self, size):
        """ Doctring """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """ str """
        return ("[Square] {}/{}".format(self.__size, self.__size))
