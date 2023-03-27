#!/usr/bin/python3
import sys

# A function that prints an integer


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as v:
        err = "Exception: " + str(v)
        print(err, file=sys.stderr)
        return False
