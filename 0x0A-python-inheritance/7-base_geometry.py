#!/usr/bin/python3
"""Code defines a class BaseGeometry."""


class BaseGeometry:
    """The class body."""

    def area(self):
        """it is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate parameter format.
            TypeError: If value is not int.
            ValueError: If value <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
