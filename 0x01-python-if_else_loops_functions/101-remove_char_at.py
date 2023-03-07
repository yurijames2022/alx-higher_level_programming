#!/usr/bin/python3
# A function that copies a string and removes its character at position n
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str
    str_list = list(str)
    del str_list[n]
    str_cpy = ''.join(str_list)
    return str_cpy
