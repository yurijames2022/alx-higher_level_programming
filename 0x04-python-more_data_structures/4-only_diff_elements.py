#!/usr/bin/python3
# A function that returns a set of all elements present in only one set

def only_diff_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    result = set_1 ^ set_2
    return result
