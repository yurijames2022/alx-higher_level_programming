#!/usr/bin/python3
# A function that converts lowercase to uppercase
def uppercase(str):
    result = ''
    for ch in str:
        if ord('a') <= ord(ch) <= ord('z'):
            ch = chr(ord(ch) - 32)
            result += ch
        else:
            result += ch
    print("{}".format(result))
