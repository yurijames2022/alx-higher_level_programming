#!/usr/bin/python3
'''
This module has a function named: say_my_name
The function prints 'My name is <first name> <last name>'
Returns: Returns nothing
'''


def say_my_name(first_name, last_name=""):
    '''
    Function that prints first and last name
    Args:
        first_name (str): First parameter
        last_name (str): Second parameter
    '''

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
    
