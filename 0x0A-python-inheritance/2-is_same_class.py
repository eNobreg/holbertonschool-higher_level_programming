#!/usr/bin/python3
""" Module """


def is_same_class(obj, a_class):
    return issubclass(a_class, type(obj))
