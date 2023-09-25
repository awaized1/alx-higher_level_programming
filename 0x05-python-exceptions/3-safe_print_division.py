#!/usr/bin/python3

def safe_print_division(a, b):
    """Code returns result of a divided by b."""
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
