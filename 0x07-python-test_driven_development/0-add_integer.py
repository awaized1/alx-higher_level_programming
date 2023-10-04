#!/usr/bin/python3
"""
This module defines an integer addition function.
"""


def add_integer(a, b=98):
    """
    Return the integer addition of 'a' and 'b'.

    Float arguments are typecasted to integers before performing the addition.

    Args:
        a (int, float): First number.
        b (int, float): Second number (default is 98).

    Returns:
        int: The integer sum of 'a' and 'b'.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or a float.

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
