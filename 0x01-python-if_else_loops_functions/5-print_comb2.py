#!/usr/bin/python3
# A program that prints numbers from 0-99
for number in range(100):
    if number == 99:
        print("{}".format(number), end='\n')
    else:
        print("{}".format(number), end=', ')
