#!/usr/bin/python3

"""
A class named base
"""


class Base():
    """ A class named Base """

    __nb_objects = 0

    def __init__(self, id=None):
        """ The initializer

        Args:
        id (int): an id argument

        """
        if id is not None:
            self.id = id
        else:
           Base. __nb_objects += 1
           self.id = Base.__nb_objects
