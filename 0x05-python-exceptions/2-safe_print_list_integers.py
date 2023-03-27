#!/usr/bin/python3

# A function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
        i = 0
        while i < x:
                try:
                        print("{:d}".format(my_list[i]), end = '' if i <= (x - 1) else '\n')
                        i += 1
                except ValueError:
                              continue;
                except IndexError:
                              pass;
        return i
