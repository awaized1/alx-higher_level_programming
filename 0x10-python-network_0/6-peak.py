#!/usr/bin/python3
"""Code finds peak in list of unsorted integers"""


def find_peak(list_of_integers):
    """Function finds peak in list_of_integers"""

    if list_of_integers is None or list_of_integers == []:
        return None
    loy = 0
    hi = len(list_of_integers)
    mid = ((hi - loy) // 2) + loy
    mid = int(mid)
    if hi == 1:
        return list_of_integers[0]
    if hi == 2:
        return max(list_of_integers)
    if list_of_integers[mid] >= list_of_integers[mid - 1] and\
            list_of_integers[mid] >= list_of_integers[mid + 1]:
        return list_of_integers[mid]
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid + 1]:
        return find_peak(list_of_integers[mid:])
    if mid > 0 and list_of_integers[mid] < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
