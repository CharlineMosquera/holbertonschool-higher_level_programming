#!/usr/bin/python3
"""JSON representation"""
import json


def load_from_json_file(filename):
    """function that creates an Object from a “JSON file”"""
    with open(filename) as file:
        return(json.loads(file.read()))
