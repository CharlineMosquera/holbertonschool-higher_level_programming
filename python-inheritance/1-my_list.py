#!/usr/bin/python3
"""definition of a subclass"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        print(sorted(self))
