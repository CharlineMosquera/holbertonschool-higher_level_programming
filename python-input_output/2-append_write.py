#!/usr/bin/python3
"""function that write a file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)"""
    with open(filename, "a", encoding="utf-8") as file:
        return(file.write(text))
