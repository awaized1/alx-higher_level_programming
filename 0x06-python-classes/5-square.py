#!/usr/bin/python3
"""Code defs a class named Square."""


class Square:
    """def of a square."""

    def __init__(self, size):
        """def initializes a new square.

        Arguments:
            size (int): The size of new square.
        """
        self.size = size

    @property
    def size(self):
        """Gets the current square. size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Code return the current square area."""
        return (self.__size * self.__size)

    def my_print(self):
        """Prints square with #."""

        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
