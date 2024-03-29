#!/usr/bin/python3
"""
A function that writes a string to a text file and returns \
the number of characters written.
"""


def append_write(filename="", text=""):
    """ A function that writes to a txt file and returns no of chars written.

    Args:
    filename (str): The file destination.
    text (str): The text to write to file

    Returns:
    No of characters written.

    """

    charCount = 0

    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)

    return len(text)
