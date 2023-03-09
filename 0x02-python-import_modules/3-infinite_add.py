#!/usr/bin/python3
import sys
# A program that prints the result of the addition of all arguments
store = 0
for i in sys.argv:
    store += i
print(store)
