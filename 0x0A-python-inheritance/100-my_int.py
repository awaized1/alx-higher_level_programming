#!/usr/bin/python3
"""Code defines class MyInt that inherits from an int."""


class MyInt(int):
    """Class invert int operators == and !=."""

    def __eq__(self, value):
        """Function, Override == opeartor with != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Function, Override != operator with == behavior."""
        return self.real == value
