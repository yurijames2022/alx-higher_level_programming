#!/usr/bin/python3
# A program that prints numbers from 0-99
for number in range(100):
    if number != 99:
        print("{0:02d}".format(number), end=', ')
    else:
        print("{0:02d}".format(number))
