#!/usr/bin/python3
"""function that lists the attributes and methods of an instance"""


def lookup(obj):
    """returns a list of available attributes and methods of an object"""
    return(dir(obj))
