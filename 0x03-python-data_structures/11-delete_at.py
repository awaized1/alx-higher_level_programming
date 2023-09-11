#!/usr/bin/python3
# 11-delete_at.py code


def delete_at(my_list=[], idx=0):
    """Code deletes item at a specific position in the list."""
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return (my_list)
