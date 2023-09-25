#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """Print x no of elememts in list.
    Arguments:
        my_list (list): List to print the elements from.
        x (int): Counts the elements of my_list to be print.

    Returns:
        Number of elements printed.
    """
    num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)
