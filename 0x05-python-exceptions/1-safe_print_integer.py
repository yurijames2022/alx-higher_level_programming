#!/usr/bin/python3

# A function that safely prints integer values

def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
