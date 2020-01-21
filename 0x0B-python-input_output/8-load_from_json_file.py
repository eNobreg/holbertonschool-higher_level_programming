#!/usr/bin/python3
""" Json module """


import json


def load_from_json_file(filename):
    """ Open """
    with open(filename, "r", encoding='utf8') as f:
        json_file = json.load(f)
        return json_file
