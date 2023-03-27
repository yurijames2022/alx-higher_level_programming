#!/usr/bin/python3
import sys
# A function that executes a function safely


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except (IndexError, ZeroDivisionError, ValueError, TypeError) as e:
        err = "Exception: " + str(e)
        print(err, file=sys.stderr)
        return None
