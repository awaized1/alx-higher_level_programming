#!/usr/bin/python3
# 3-say_my_name.py
"""Code defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Function print a name.

    Arguments:
        first_name (str): Name to be printed first.
        last_name (str): Name to be printed last.
    Raises:
        TypeError: If either of first_name or last_name aren't strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
