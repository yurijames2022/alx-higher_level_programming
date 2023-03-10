#!/usr/bin/python3
'''
 A function that returns a tuple
 with the length of a string
 and its first character
'''


def multiple_returns(sentence):

    result = ()
    if len(sentence) == 0:
        sentence[0] = None

    result = len(sentence), sentence[0]
    return result
