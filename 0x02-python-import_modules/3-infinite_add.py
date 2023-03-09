#!/usr/bin/python3
import sys
# A program that prints the result of the addition of all arguments
del sys.argv[0]

store = 0
for i in sys.argv:
    i = int(i)
    store += i
print(store)
