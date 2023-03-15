#!/usr/bin/python3
# A function that prints a dictionary by ordered keys

def print_sorted_dictionary(a_dictionary):
    sorted_keys = sorted(a_dictionary.keys())
    for k in sorted_keys:
        v = a_dictionary[k]
        print("{}: {}".format(k, v))
