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

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Returns the area of Rectangle. """

        return self.__width * self.__height

    def __str__(self):
        """str magic function"""

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
