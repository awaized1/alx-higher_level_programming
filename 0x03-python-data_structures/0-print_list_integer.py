#!/usr/bin/python3
# 0-print_list_integers.py


def print_list_integer(my_list=[]):
    """Code prints all integers of the list."""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
