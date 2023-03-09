#!/usr/bin/python3
if __name__ == '__main__':
    import sys

del sys.argv[0]
len_args = len(sys.argv)

if len_args == 0:
    print("{} arguments.".format(len_args))
elif len_args == 1:
    print("{} argument:".format(len_args))
else:
    print("{} arguments:".format(len_args))
for arg in range(len_args):
    print("{}: {}".format(arg + 1, sys.argv[arg]))
