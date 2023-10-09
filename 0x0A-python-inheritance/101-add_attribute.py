#!/usr/bin/python3
"""Code define a function attributes."""


def add_attribute(obj, att, value):
    """Function adds a new attribute to object if possible.
    Raises:
        TypeError: If attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
