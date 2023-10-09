#!/usr/bin/python3
"""Code defines a Rectangle module."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class of body."""

    def __init__(self, size):

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
