#!/usr/bin/python3
# A function that checks for lowercase character
def islower(c):
    low_var = ord(c)
    if low_var in range(97, 122):
        return True
    else:
        return False
