#!/usr/bin/python3
# A function that prints all integers of a list
# in reversed order
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        print("{}".format(i))
    return my_list
