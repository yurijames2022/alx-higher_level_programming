#!/usr/bin/python3
# A function that finds the biggest integer of a list
def max_integer(my_list=[]):
    max_val = -10000000000000000000000000000000000000
    if my_list == []:
        return None
    for i in my_list:
        if i > max_val:
            max_val = i
    return max_val
