#!/usr/bin/python3
"""
An empty class named BaseGeometry
"""


class BaseGeometry(object):
    """ An empty class named BaseGeometry """

    def area(self):
        """ A function that raises an exception.
        Exceptions:
        raises Exception

        """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """A function that validates name and value types.

        Args:
        name (str): The name
        value (int): The value

        Returns:
        no returns

        Exceptions:
        TypeError - When value is not integer type
        ValueError - When value is less or equal to zero
        """

        self.name = name
        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        else:
            self.value = value
