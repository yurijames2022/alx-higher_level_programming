#!/usr/bin/python3
import sys

del sys.argv[0]
number = 0
len_args = len(sys.argv)

if len_args == 1:
    print("{} argument:".format(len_args))
    print("{}: {}".format(len_args, sys.argv[0]))
if len_args == 0:
    print("{} arguments.".format(len_args))
if len_args != 0 and len_args != 1:
    print("{} arguments:".format(len_args))
    for i in sys.argv:
        number += 1
        print("{}: {}".format(number, i))
