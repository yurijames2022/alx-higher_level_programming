#!/usr/bin/python3

''' A class named rectangle '''


class Rectangle:
    ''' A rectangle class '''
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        ''' width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width setter '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        ''' height property '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height setter '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        ''' Area '''
        return self.width * self.height

    def perimeter(self):
        ''' Perimeter '''
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return 2 * (self.width + self.height)

    def __str__(self):
        ''' str '''
        if self.width == 0 or self.height == 0:
            return ""
        else:
            rectangle_str = ""
            for i in range(self.height):
                rectangle_str += "#" * self.width + "\n"
            return rectangle_str[:-1]

    def __repr__(self):
        ''' repr '''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        ''' deleter '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
