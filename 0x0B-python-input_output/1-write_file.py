#!/usr/bin/python3
"""
A function that writes a string to a text file and returns \
the number of characters written.
"""


def write_file(filename="", text=""):
    """ A function that writes to a txt file and returns no of chars written.

    Args:
    filename (str): The file destination.
    text (str): The text to write to file

    Returns:
    No of characters written.

    """

    charCount = 0

    with open((filename), "w", encoding="utf-8") as f:
        f.write((text))

    with open((filename), "r", encoding="utf-8") as f:
        for line in f:
            charCount += len(line)

    return charCount
