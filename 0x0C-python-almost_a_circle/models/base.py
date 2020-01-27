#!/usr/bin/python3
""" Module for Base class of Almost a Circle """

import turtle
from os.path import exists
import json


class Base:
    """ Base Class for almost a circle """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantaiation Constructor method """
        if id is not None:
            self.id = id
        elif not id:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'
        """
        ld = list_dictionaries
        return ("[]" if ld is None or len(ld) == 0 else json.dumps(ld))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to a file"""
        if list_objs is None:
            list_objs = []
        new = []
        for entry in list_objs:
            new.append(entry.to_dictionary())
        with open(cls.__name__ + '.json', 'w') as f:
            f.write(cls.to_json_string(new))

    @staticmethod
    def from_json_string(json_string):
        """ This
        if json_string is None:
            return []
        """
        js = json_string
        return ([] if js is None or not js else json.loads(js))

    @classmethod
    def create(cls, **dictionary):
        """ Create a new instance """
        if cls.__name__ == "Rectangle":
            new = cls(5, 5)
        elif cls.__name__ == "Square":
            new = cls(5)
        new.update(**dictionary)
        return(new)

    @classmethod
    def load_from_file(cls):
        """ Load from File  """
        listl = []
        if not exists(cls.__name__ + ".json"):
            return []
        with open(cls.__name__ + ".json") as f:
            new = cls.from_json_string(f.read())
        return [cls.create(**entry) for entry in new]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw a turtle """
        wn = turtle.Screen()
        alex = turtle.Turtle()
        alex.forward(50)
        alex.left(90)
        turtle.exitonclick()
