#!/usr/bin/python3
# A function that removes all characters c and C from a string
def no_c(my_string):
    no_c = ''
    for letter in my_string:
        if letter != 'c' and letter != 'C':
            no_c += letter
    return no_c
