#!/usr/bin/python3
""" Class to Json """


class Student():
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Instantiation for class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ json repr """
        if type(attrs) is list and all([isinstance(x, str) for x in attrs]):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        else:
            return self.__dict__
