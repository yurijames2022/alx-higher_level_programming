#!/usr/bin/python3
"""
A function that returns True if the object is an instance of a class that \
inherited (directly or indirectly) from the specified class, otherwise False.
"""


def inherits_from(obj, a_class):
    """Function that checks for inheritance of a class directly or indirectly

    Args:
    obj (any): The object.
    a_class: The class inherited from.

    Returns:
    if inherited returns - True
    otherwise returns - False

    """

    if (isinstance(obj, a_class) and type(obj) != a_class):
        return True
    return False
