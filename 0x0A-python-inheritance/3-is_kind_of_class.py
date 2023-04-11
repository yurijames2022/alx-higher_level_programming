#!/usr/bin/python3
"""A function that checks for relationship between obj and a_class. """


def is_kind_of_class(obj, a_class):
    """ Function that checks for instance

    Args:
    obj (any): The object
    a_class: The class

    Returns:
    if is instance returns - True
    else returns - False

    """

    if isinstance(obj, a_class):
        return True
    return False
