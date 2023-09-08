#!/usr/bin/python3


def magic_calculation(a, b):
    """Code matches byte code from Holberton School."""
    from magic_calculation_102 import add, sub

    if a < b:
        d = add(a, b)
        for i in range(4, 6):
            d = add(d, i)
        return (d)

    else:
        return(sub(a, b))
