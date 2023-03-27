#!/usr/bin/python3

# A function that prints the first x elements of a list and only integers

def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            if isinstance(i, int):
                print("{:d}".format(i), end='')
                count += 1
        except TypeError:
            pass
        if count == x:
            break
    print()
    return count
