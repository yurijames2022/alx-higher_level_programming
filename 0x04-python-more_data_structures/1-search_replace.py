#!/usr/bin/python3
'''
A function that replaces all occurrences of an element
by another in a new list

'''


def search_replace(my_list, search, replace):
    my_list = []
    new_list = my_list.copy
    for i in new_list:
        if i == search:
            i = replace
    return new_list
