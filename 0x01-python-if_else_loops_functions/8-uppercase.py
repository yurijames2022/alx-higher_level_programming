#!/usr/bin/python3
# A function that converts lowercase to uppercase
def uppercase(str):
    str_len = len(str)
    for ch in str:
        if 'a' <= ch <= 'z':
            print(chr(ord(ch)-32), end='' if str_len else '\n')
        else:
            print("{}".format(ch), end='' if str_len else '\n')
    print()
