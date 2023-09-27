#!/usr/bin/python3
"""Code defines a class named Square."""


class Square:
    """Class reps a square."""

    def __init__(self, size=0):
        """Code initialize a new Square.

        Arguments:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
