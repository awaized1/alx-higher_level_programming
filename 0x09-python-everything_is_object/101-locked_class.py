#!/usr/bin/python3
"""Defines a class with restricted attribute creation."""

class LockedClass:
    """
    This class restricts attribute creation to only 'first_name'.
    Any attempts to create other attributes will raise an error.
    """

    __slots__ = ["first_name"]
