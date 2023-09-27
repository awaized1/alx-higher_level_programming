#!/usr/bin/python3
"""Defs a class named Square."""

class Square:
    """Reps a square."""

    def __init__(self, size=0):
        """Code initializes a new square.

        Arguments:
            size (int): Size of the new square.
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
        """Code returns the area of the square."""
        return (self.__size * self.__size)

    def __eq__(self, other):
        """Define the equal to comparision to a Square."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Define the not equal to comparison to a Square."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Define the less than comparison to a Square."""
        return self.area() < other.area()

    def __le__(self, other):
        """Define the less tha euqal comparison to a Square."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Define the greater than comparison to a Square."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Define the greater equal to compmarison to a Square."""
        return self.area() >= other.area()
