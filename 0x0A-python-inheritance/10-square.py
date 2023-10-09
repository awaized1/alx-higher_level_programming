#!/usr/bin/python3
"""Code defines a rectangle subclass square."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class represent a square."""

    def __init__(self, size):
        """Finction initializes new square.

        Args:
            size (int): Size of new square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
