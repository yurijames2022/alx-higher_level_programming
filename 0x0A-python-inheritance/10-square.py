#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
A class Square that inherits fr0m class Rectangle
"""


class Square(Rectangle):
    """ A class named square that inherits from Rectangle """

    def __init__(self, size):
        """ Initializer function

        Args:
        size (int): The size
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
