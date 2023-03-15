#!/usr/bin/python3
# A function that returns a set of common elements in two sets

def common_elements(set_1, set_2):
    set_1 = set(set_1)
    set_2 = set(set_2)
    result = set_1 & set_2
    return result
