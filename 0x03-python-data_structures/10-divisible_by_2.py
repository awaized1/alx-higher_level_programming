#!/usr/bin/python3
# 10-divisible_by_2.py code

def divisible_by_2(my_list=[]):
    """Code finds all multiples of 2 in list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)

    return (multiples)
