#!/usr/bin/python3
"""Validates whether it is an instance or a subclass"""


def is_kind_of_class(obj, a_class):
    """function returns whether the object belongs
    to a class or is an inherited class"""
    if type(obj) is type(a_class):
        return issubclass(obj, a_class)
    return isinstance(obj, a_class)
