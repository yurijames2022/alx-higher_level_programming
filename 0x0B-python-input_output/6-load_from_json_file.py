#!/usr/bin/python3
""" A function that creates an object from a JSON file """
import json


def load_from_json_file(filename):
    """ A function that creates an object from a JSON file

    Args:
    filename (str): The file destination

    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
