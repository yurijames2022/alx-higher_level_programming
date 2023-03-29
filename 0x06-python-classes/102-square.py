#!/usr/bin/python3

'''
Writing a class that defines a square
'''


class Square:
    ''' A class named Square that can return area '''
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''Returns: The square of the size '''
        return (self.__size ** 2)

    def __eq__(self, other):
        ''' For equal to '''
        return self.area() == other.area()

    def __ne__(self, other):
        ''' For not equal to '''
        return self.area() != other.area()

    def __gt__(self, other):
        ''' For greater than '''
        return self.area() > other.area()

    def __ge__(self, other):
        ''' For greater than or equal to '''
        return self.area() >= other.area()

    def __lt__(self, other):
        ''' For less than '''
        return self.area() < other.area()

    def __le__(self, other):
        ''' For less than or equal to '''
        return self.area() <= other.area()
