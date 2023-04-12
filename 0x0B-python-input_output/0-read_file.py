#!/usr/bin/python3
""" A function that reads a text file """


def read_file(filename=""):
    """ A function that reads a text file and prints it to stdout.

    Args:
    filename (str): The file destination of the file to be read.

    """

    with open((filename), "r", encoding="utf-8") as my_file:
        print(my_file.read(), end="")
