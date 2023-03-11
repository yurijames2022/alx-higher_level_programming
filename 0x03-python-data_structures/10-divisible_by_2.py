#!/usr/bin/python3
# A function that finds all multiples of 2 in a list
def divisible_by_2(my_list=[]):
    bool_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            bool_list.append(True)
        elif my_list[i] % 2 != 0:
            bool_list.append(False)
    return bool_list
