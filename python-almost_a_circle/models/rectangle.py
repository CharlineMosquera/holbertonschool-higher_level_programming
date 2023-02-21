#!/usr/bin/python3
"""Module Rectangle that inherits from Base"""
from models.base import Base


def validate_attributes(value, attribute):
    """method to validate attributes"""
    if not isinstance(value, int):
        raise TypeError(f"{attribute} must be an integer")
    if attribute == "width" and value <= 0:
        raise ValueError("width must be > 0")
    if attribute == "height" and value <= 0:
        raise ValueError("height must be > 0")
    if attribute == "x" and value < 0:
        raise ValueError("x must be >= 0")
    if attribute == "y" and value < 0:
        raise ValueError("y must be >= 0")


class Rectangle(Base):
    """class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        validate_attributes(width, "width")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        validate_attributes(height, "height")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        validate_attributes(x, "x")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        validate_attributes(y, "y")
        self.__y = y

    def area(self):
        return self.__width * self.__height
