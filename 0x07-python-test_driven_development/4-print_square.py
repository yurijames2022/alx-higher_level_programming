#!/usr/bin/python3
'''
This module has a print square function
It prints the square of a number in a '#' grid
Returns: nothing
'''


def print_square(size):
    '''
    Prints square of size
    Args:
        size (int): The size of the square
    '''
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        for row in range(size):
            print("#" * size)
