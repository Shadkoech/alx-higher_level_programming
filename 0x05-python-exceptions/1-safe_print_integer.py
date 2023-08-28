#!/usr/bin/python3


def safe_print_integer(value):
    """Function printing an integer using the "{:d}".format()"""

    try:
        print("{:d}".format(value))
        return True

    except (ValueError):
        return False
