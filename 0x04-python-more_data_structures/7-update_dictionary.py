#!/usr/bin/python3
# A function that replaces or adds key/value in a dictionary

def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        a_dictionary[key] = value
    else:
        a_dictionary[key] = value
    return a_dictionary
