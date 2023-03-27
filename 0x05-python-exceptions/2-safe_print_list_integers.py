#!/usr/bin/python3

# A function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
        i = 0
        for val in range(x):
            try:
                print("{:d}".format(my_list[i]), end='' if i < x else '\n')
                i += 1
            except (ValueError, TypeError):
                continue
        return i
