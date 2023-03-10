#!/usr/bin/python3
'''
 A function that returns a tuple
 with the length of a string
 and its first character
'''


def multiple_returns(sentence):

    result = ()
    if sentence == '':
        result = (len(sentence), None)
    else:
        result = len(sentence), sentence[0]
    return result
