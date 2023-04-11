#!/usr/bin/bash
''' A function that checks for instance '''


def is_kind_of_class(obj, a_class):
    ''' Function that checks for instance
    Args:
    obj: The object
    a_class: The class

    Returns:
    Returns True if isinstance.
    False if not
    '''

    if isinstance(obj, a_class):
        return True
    else:
        return False
