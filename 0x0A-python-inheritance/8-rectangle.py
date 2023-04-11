#!/usr/bin/python3
"""
A class Rectangle that inherits from BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A class rectangle that inherits from class BaseGeometry. """

    def __init__(self, width, height):
        """ The initializer function.
        Args:
        width (int): The width
        height (int): The height

        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
