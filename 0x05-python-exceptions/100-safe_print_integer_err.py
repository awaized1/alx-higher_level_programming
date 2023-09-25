#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    """Code prints int with "{:d}".format().

    If ValueError message, a message
    is printed to stderr.

    Args:
        value (int): int

    Returns:
        If TypeError or ValueError - False.
        O/W - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
