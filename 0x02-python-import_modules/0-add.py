#!/usr/bin/python3
import sys
if __name__ == '__main__':
    from add_0 import add
else:
    sys.exit()

a = 1
b = 2
print("{} + {} = {}".format(a, b, add(a, b)))
