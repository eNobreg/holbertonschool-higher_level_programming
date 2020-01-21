#!/usr/bin/python3
""" Module """

import json


def to_json_string(my_obj):
    """ Convert to json"""
    json_file = json.dumps(my_obj)
    return json_file
