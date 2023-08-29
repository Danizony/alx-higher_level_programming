#!/usr/bin/python3

def safe_print_integer(value):
    try:
        the_output = "{:d}".format(int(value))
        print(the_output)
        return True
    except ValueError:
        return False
