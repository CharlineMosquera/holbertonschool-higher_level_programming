#!/usr/bin/python3
"""Module class Base"""


class Base():
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id != None:
            self.id = id
        Base.__nb_objects += 1
        self.id = Base.__nb_objects
