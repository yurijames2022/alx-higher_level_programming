#!/usr/bin/python3
""" Function that checks for instance """


def is_same_class(obj, a_class):
    ''' Function that checks if obj is an instance of a_class

    Args:
    obj: The object
    a_class: The class

    Returns: Returns True if isinstance. False if not
    '''

    if type(obj) == a_class:
        return True
    else:
        return False
