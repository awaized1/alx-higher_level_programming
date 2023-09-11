#!/usr/bin/python3
# 8-multiple_returns.py code


def multiple_returns(sentence):
    """Code returns length of string and its first char."""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
