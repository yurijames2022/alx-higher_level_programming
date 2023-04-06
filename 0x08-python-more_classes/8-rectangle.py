#!/usr/bin/python3

''' A class named rectangle '''


class Rectangle:
    ''' A rectangle class '''
    number_of_instances = 0
    print_symbol = '#'

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
            return (str(self.print_symbol) * self.width + '\n') * self.height

    def __repr__(self):
        ''' repr '''
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        ''' deleter '''
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            Return the biggest rectangle based on the area

            Args:
                rect_1 (Rectangle): Rectangle 1
                rect_2 (Rectangle): Rectangle 2

            Raises:
                TypeError: If rect_1 is not an instance of Rectangle
                TypeError: If rect_2 is not an instance of Rectangle

            Returns:
                The biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
