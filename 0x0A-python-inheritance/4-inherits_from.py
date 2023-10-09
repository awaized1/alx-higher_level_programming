#!/usr/bin/python3
"""Code defines inherited class-checking function."""


def inherits_from(obj, a_class):
    """Function checks if object is an inherited instance of class.

    Args:
        obj (any): Object to check.
        a_class (type): Class to match type of object to.
    Returns:
        If obj is inherited instance of a_class - True.
        O/W - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
