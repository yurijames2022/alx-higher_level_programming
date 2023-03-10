#!/usr/bin/python3
# A function that replaces an element in a list at a specific position
# without modifying the original list (like in C)
def new_in_list(my_list, idx, element):
    list_cpy = my_list.copy()
    if idx < 0 or idx > len(my_list):
        return list_cpy
    else:
        list_cpy[idx] = element
        return list_cpy
