#!/usr/bin/python3
# A program that prints numbers from 0-99
for i in range(10):
    for j in range(10):
        if (i == 9 and j == 9):
            print("{}{}".format(i, j), end='\n')
        else:
            print("{}{}".format(i, j), end=', ')
