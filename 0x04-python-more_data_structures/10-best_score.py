#!/usr/bin/python3
# A function that returns a key with the biggest integer value

def best_score(a_dictionary):
    if a_dictionary.keys():
        biggest = max(a_dictionary.values())
        for i in a_dictionary:
            dict_keys = list(a_dictionary.keys())
            if biggest == a_dictionary[i]:
                return dict_keys[i]
