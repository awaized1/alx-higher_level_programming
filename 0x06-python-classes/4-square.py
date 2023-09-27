#!/usr/bin/python3
"""Code define a class named Square."""


class Square:
    """class reps a square."""

    def __init__(self, size=0):
        """def initialize new square.

        Arguments:
            size (int): Size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Code return current area of square."""
        return (self.__size * self.__size)
