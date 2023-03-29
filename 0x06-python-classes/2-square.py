#!/usr/bin/python3

'''
Writing a class that defines a square
'''


class Square:
    ''' A class that defines a square '''

    def __init__(self, size=0):
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")

        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")
