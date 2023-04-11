#!/usr/bin/python3
''' A class MyList that inherits fr0m list '''


class MyList(list):
    ''' A class that inherits from class list '''
    def print_sorted(self):
        ''' A function that prints the list in sorted manner '''

        sorted_list = sorted(self)
        print(sorted_list)
