#!/usr/bin/python3
"""function that prints a square"""


def print_square(size):
    """Prints the square using the character '#'"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size == 0:
        print("")
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print("#", end="")
        print("")
