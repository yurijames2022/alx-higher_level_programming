#!/usr/bin/bash
""" A class MyInt that inherits from int """


class MyInt(int):
    """ class MYInt that inherits from int """

    def __eq__(self, other):
        return int(self) != int(other)

    def __ne__(self, other):
        return int(self) == int(other)
