#!/usr/bin/python3


def safe_print_integer(value):
    """Function prints integer using "{:d}".format().
    Args:
        value (int): Integer to be printed

    Returns:
        If ValueError or TypeError - False.
        O/W - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
