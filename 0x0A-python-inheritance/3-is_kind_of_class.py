#!/usr/bin/python3
"""An inherited class-checking function."""


def is_kind_of_class(obj, a_class):
    """Checks if object is an instance or inherited instance of class.
    Args:
        obj (any): The object to check for.
        a_class (type): Class to compare type of obj to.
    Returns:
        Boolean of an the instance.
    """
    if isinstance(obj, a_class):
        return True
    return False
