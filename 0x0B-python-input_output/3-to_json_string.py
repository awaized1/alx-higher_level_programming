#!/usr/bin/python3
"""Code defines to_json_string module """

import json


def to_json_string(my_obj):
    """
    Function returns the JSON representation of object (string)
    """

    return json.dumps(my_obj)
