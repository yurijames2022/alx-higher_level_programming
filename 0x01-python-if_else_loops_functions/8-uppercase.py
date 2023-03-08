#!/usr/bin/python3
# A function that converts lowercase to uppercase
def uppercase(str):
    for character in str:
        if 'a' <= character <= 'z':
            print(chr(ord(character) - 32), end='')
        else:
            print(character, end='')
    print()
