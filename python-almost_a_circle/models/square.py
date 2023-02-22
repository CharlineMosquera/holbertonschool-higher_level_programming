#!/usr/bin/python3
"""Module Square that inherits from Rectangle"""
from models.rectangle import Rectangle, validate_attributes


class Square(Rectangle):
    """class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        validate_attributes(value, "width")
        self.__width = value
        self.__height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        """updates the values of the instance's attributes"""
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for attribute, value in zip(attributes, args):
                setattr(self, attribute, value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
