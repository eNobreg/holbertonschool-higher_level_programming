#!/usr/bin/python3
""" This class """


class MyList(list):
    """ print """

    def print_sorted(self):
        """ Docstring """
        print("{}".format(sorted(self)))
