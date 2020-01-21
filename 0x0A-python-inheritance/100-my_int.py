#!/usr/bin/python3
""" Rebel int module """


class MyInt(int):
    """ Rebel int """

    def __ne__(self, value):
        """ Not equal """
        return int(self) == int(value)

    def __eq__(self, value):
        """ Self """
        return int(self) != int(value)
