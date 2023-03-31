#!/usr/bin/python3
''' add_integer function
It takes two arguments a and b and adds them
The function can take only int and float data types
Returns the sum of a and b
'''


def add_integer(a, b=98):
    '''Args:
    a: The first parameter
    b: The second parameter '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
