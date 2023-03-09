#!/usr/bin/python3
'''
Write a program that imports all functions from the file calculator_1.py
and handles basic operations.

'''
if __name__ == '__main__':
    from calculator_1 import add, sub, div, mul
    import sys

del sys.argv[0]
args_list = sys.argv
len_args = len(args_list)

if len_args != 3:
    print(r"Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = ['+', '-', '*', '/']


if args_list[1] not in operator:
    print(r"Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

if args_list[1] == '+':
    a = int(args_list[0])
    b = int(args_list[2])
    print("{} {} {} = {}".format(a, args_list[1], b, add(a, b)))

if args_list[1] == '-':
    a = int(args_list[0])
    b = int(args_list[2])
    print("{} {} {} = {}".format(a, args_list[1], b, sub(a, b)))

if args_list[1] == '*':
    a = int(args_list[0])
    b = int(args_list[2])
    print("{} {} {} = {}".format(a, args_list[1], b, mul(a, b)))

if args_list[1] == '/':
    a = int(args_list[0])
    b = int(args_list[2])
    print("{} {} {} = {}".format(a, args_list[1], b, div(a, b)))
