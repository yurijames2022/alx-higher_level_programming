#!/usr/bin/python3
# A program that prints alphabet except q and e

for alphabet in range(97, 123):
    if alphabet != 101 and alphabet != 113:
        print("{}".format(chr(alphabet)), end='')
