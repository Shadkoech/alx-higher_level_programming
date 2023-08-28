#!/usr/bin/python3


def safe_print_integer_err(value):
    """This is a function printing an integer"""

    from sys import stderr

    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        print("Exception: {}".format(sys.exc_info()[1]), file=stderr)
        return False
