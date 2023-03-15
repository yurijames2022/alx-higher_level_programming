#!/usr/bin/python3
# A function that returns a new dictionary with all values multiplied by 2

def multiply_by_2(a_dictionary):
    cpy_dict = a_dictionary.copy()
    dict_list = list(cpy_dict.keys())
    for k in dict_list:
        v = cpy_dict[k] * 2
        cpy_dict[k] = v
    return cpy_dict
