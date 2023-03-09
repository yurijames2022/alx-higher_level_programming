#!/usr/bin/python3
import sys
# A program that prints the result of the addition of all arguments
len_args = len(sys.argv)
result = 0
j = 0
for i in range(len_args):
    if i != sys.argv[0]:
        j = int(sys.argv[i])
        result += j
print("{}".format(result))
