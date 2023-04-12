#!/usr/bin/python3
""" A function that returns an object represented by a JSON string """
import json


def from_json_string(my_str):
    """ A function that returns a python ds represented by a JSON string.

    Args:
    my_str (str): The string to be returned

    Returns:
    Returns the object represented by JSON string

    """

    return json.loads(my_str)
