#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Code executes function

    Args:
        fct: Function to be executed.
        args: Args for function.

    Returns:
        If err occurs - None.
        O/W - the result of function.
    """
    try:
        result = fct(*args)
        return (result)
    except:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (None)
