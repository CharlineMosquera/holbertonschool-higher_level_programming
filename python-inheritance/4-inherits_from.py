#!/usr/bin/python3
"""valid subclass"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) != a_class
