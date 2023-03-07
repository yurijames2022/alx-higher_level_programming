#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
last_str = 'Last digit of '
greater = ' and is greater than 5'
less_than = 'and is less than 6 and not 0'
if number > 0:
    if last_digit > 5:
        print('{}{} is {}{}'.format(last_str, number, last_digit, greater))
    elif last_digit == 0:
        print("Last digit of {} is {} and is zero".format(number, last_digit))
    elif last_digit < 6:
        print("{} {} is {} {}".format(last_str, number, last_digit, less_than))

elif number < 0:
    number_neg = abs(number)
    last_digit = number_neg % 10
    if last_digit > 5:
        print("{}{} is {}{}".format(last_str, number, last_digit, greater))
    if last_digit == 0:
        print("Last digit of {} is {} and is zero".format(number, last_digit))
    elif last_digit < 6:
        print("{} {} is {} {}".format(last_str, number, last_digit, less_than))
