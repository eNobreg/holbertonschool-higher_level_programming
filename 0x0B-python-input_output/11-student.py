#!/usr/bin/python3
""" Class to Json """


class Student():
    """ Student Class """

    def __init__(self, first_name, last_name, age):
        """ Instantiation for class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ json repr """
        return(self.__dict__)
