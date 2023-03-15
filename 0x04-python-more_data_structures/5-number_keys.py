#!/usr/bin/python3
# A function that returns the number of keys in a dictionary

def number_keys(a_dictionary):
    length_dict = 0
    for i in a_dictionary.keys():
        length_dict += 1
    return length_dict
