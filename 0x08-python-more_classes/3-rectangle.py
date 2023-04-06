#!/usr/bin/python3

''' An empty class named rectange '''


class Rectangle:
    ''' A rectangle class '''
    @property
    def width(self):
        ''' The property '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' The setter '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' The property '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' The setter '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        ''' Method for returning area '''
        return (self.__width * self.__height)

    def perimeter(self):
        ''' The Perimeter'''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.__width + self.__height) * 2)

    def __str__(self):
        ''' str '''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += "#" * self.width + "\n"
            return rectangle_str[:-1]
