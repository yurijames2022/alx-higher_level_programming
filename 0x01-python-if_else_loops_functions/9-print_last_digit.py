#!/usr/bin/python3
# A function that prints the last digit of a number
def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print('{}'.format(last_digit), end='')
    return last_digit
