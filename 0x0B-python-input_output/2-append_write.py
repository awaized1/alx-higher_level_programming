#!/usr/bin/python3
"""Code defines file-appending function."""


def append_write(filename="", text=""):
    """Function appends string to end of a UTF8 text file.

    Args:
        filename (str): Name of file to append to.
        text (str): String to append to file.
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
