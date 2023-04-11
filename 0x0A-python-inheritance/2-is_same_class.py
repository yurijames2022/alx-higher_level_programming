#!/usr/bin/bash
'''
A function that returns true if object is an instance of specified class
'''


def is_same_class(obj, a_class):
    '''
    A function that checks for instance
    '''

    return type(obj) is a_class
