#!/usr/bin/python3
"""MyList inherits from list class"""


class MyList(list):
    """Class implements sorted printing of built-in list class"""
    def print_sorted(self):
        """prints a sorted list"""
        print(sorted(self))
