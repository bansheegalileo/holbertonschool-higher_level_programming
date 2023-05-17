#!/usr/bin/python3

def safe_print_integer(value):
    try:
        i = int(value)
        if isinstance(i, int):
            print("{:d}".format(i))
            return True
    except (TypeError, ValueError):
        return False
    return False
