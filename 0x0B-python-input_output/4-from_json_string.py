#!/usr/bin/python3
"""Code defines JSON-to-object function."""
import json


def from_json_string(my_str):
    """Function return the Python object representation of JSON string."""
    return json.loads(my_str)
