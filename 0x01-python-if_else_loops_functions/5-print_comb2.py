#!/usr/bin/python3
# A program that prints numbers from 0-99
for number in range(100):
    print("{:02d}".format(number), end=", " if number != 99 else '\n')
