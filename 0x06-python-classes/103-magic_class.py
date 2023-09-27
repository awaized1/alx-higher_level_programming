#!/usr/bin/python3
"""Code defines MagicClass matching exactly a bytecode"""

import math


class MagicClass:
    """MagicClass reps a circle."""

    def __init__(self, radius=0):
        """def initialize a MagicClass.

        Arg:
            radius (float or int): indicates radius of new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Code returns the area of MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Code returns circumference o MagicClass."""
        return (2 * math.pi * self.__radius)
