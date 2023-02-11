#!/usr/bin/python3
"""Function that adds 2 integers."""

def add_integer(a, b=98):
    """Adds two integers or floating-point numbers and returns the result as an integer."""
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return(a + b)
