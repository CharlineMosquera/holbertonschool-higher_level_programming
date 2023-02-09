#!/usr/bin/python3
"""First definition of a class"""


class Square():
    """
    Class to represent a square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of the Square class
        
        :param size: The size of the square (default is 0)
        :type size: int
        :param position: The position of the square (default is (0, 0))
        :type position: tuple of two ints
        """
        self.size = size
        self.position = position

    def area(self):
        """
        Calculates the area of the square
        
        :return: The area of the square
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """
        Gets the size of the square
        
        :return: The size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Sets the size of the square
        
        :param size_value: The size to set for the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.
        
        :return: tuple: The position of the square on a 2D plane.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """property setter for the position attribute

        Args:
        value (tuple): a tuple of 2 positive integers representing the position of the square

        Raises:
        TypeError: if value is not a tuple of 2 positive integers
        """
        if type(value) != tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints the square using the character '#'

        If the size attribute is 0, it prints an empty line.
        Otherwise, it prints the square using the '#' character,
        and taking into account the position attribute.
        """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(1, self.__size + 1):
            print(" " * self.__position[0] + "#" * self.__size)
