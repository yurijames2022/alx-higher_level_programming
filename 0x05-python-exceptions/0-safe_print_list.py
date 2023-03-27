#!/usr/bin/python3

# A function that prints x elements of a list

def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{}".format(my_list[i]), end='' if i < (x - 1) else '\n')
            i += 1
    except (IndexError, TypeError):
        print()
        pass
    return i
