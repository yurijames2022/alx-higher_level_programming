#!/usr/bin/python3
#  A function that adds 2 tuples
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    zero_holder = (0,)
    if len(tuple_a) == 0:
        tuple_a = (0, 0)
    elif len(tuple_a) < 2:
        tuple_a += zero_holder
    if len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) < 2:
        tuple_b += zero_holder
    result = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return result
