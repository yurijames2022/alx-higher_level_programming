#!/usr/bin/python3
if __name__ == '__main__':
    import sys
# A program that prints the result of the addition of all arguments
del sys.argv[0]
len_args = len(sys.argv)
arg_conv = 0
result = 0
for i in range(len_args):
    arg_conv = int(sys.argv[i])
    result += arg_conv
print("{}".format(result))
