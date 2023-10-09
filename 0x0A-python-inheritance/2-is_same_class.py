#!/usr/bin/python3
"""Code defines class-checking function."""


def is_same_class(obj, a_class):
    """Function checks if object is exactly an instance of given class.

    Args:
        obj (any): object to be checked.
        a_class (type): Class to match type of obj to.
    Returns:
        If obj is exactly an instance of the a_class - True
        O/W - False.
    """
    if type(obj) == a_class:
        return True
    return False
