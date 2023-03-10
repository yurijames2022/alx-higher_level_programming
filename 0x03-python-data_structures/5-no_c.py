#!/usr/bin/python3
# A function that removes all characters c and C from a string
def no_c(my_string):
    str_list = list(my_string)
    if 'c' in str_list:
        str_list.remove('c')
    if 'C' in str_list:
        str_list.remove('C')
    my_string = ''.join(str_list)
    return my_string
