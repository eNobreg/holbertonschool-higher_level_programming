#!/usr/bin/python3
""" Module for Base class of Almost a Circle """

from os.path import exists
import json
class Base:
    """ Base Class for almost a circle """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Instantaiation Constructor method """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '"[]"'
        new_json = json.dumps(list_dictionaries)
        return new_json
    
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
        """ This """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create a new instance """
        new = cls(5, 5)
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
            for entry in new:
                x = cls.create(**entry)
                listl.append(x)
        return listl
