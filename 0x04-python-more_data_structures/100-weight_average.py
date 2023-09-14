#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    dig = 0
    den = 0

    for tup in my_list:
        dig += tup[0] * tup[1]
        den += tup[1]

    return (dig / den)
