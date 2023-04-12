#!/usr/bin/python3
""" A function that returns the JSON representation of an object """
import json


def to_json_string(my_obj):
    """ A function that returns the JSON representation of an object

    Args:
    my_obj (str) - The object to be returned

    Returns:
    Returns the JSON representation of my_obj

    """

    return json.dumps(my_obj)
