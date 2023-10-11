#!/usr/bin/python3
"""Code defines Python class-to-JSON function."""


def class_to_json(obj):
    """Function returns dictionary represntation of the simple data structure."""
    return obj.__dict__
