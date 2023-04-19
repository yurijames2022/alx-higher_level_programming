#!/usr/bin/python3
""" A class named Rectange that inherits from Base """
from models.base import Base


class Rectangle(Base):
    """ A class named Rectangle that inherits from Base """

    @property
    def width(self):
        """ Gets width """
        return self.__width

    @width.setter
    def width(self, width):
        """ Sets width """
        self.__width = width

    @property
    def height(self):
        """ Gets height """
        return self.__height

    @width.setter
    def height(self, height):
        """ Sets height """
        self.__height = height

    @property
    def x(self):
        """ Gets x """
        return self.__x

    @width.setter
    def x(self, x):
        """ Sets x """
        self.__x = x

    @property
    def y(self):
        """ Gets Y """
        return self.__y

    @y.setter
    def y(self, y):
        """ Sets y """
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """ The initializer method
        Args:
        width (int): The width
        height (int): The height
        x (int): The value x
        y (int): The value y
        """

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
