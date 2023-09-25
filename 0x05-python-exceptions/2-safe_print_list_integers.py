#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """Code prints first x elements of integers in a list.

    Args:
        my_list (list): List to print elements from.
        x (int): Number of elements to print.

    Returns:
        No of elements printed.
    """
    num = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (num)
