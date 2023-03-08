#!/usr/bin/python3
'''
 A program that prints the ASCII alphabet
 in reverse order
 alternating lowercase and uppercase
 (z in lowercase and Y in uppercase)
 not followed by a new line.

'''

for letter in range(ord('Z'), ord('A') - 1, -1):
    if letter % 2 == 0:
        print("{}".format(chr(letter)), end='')
    else:
        print("{}".format(chr(letter).lower()), end='')
