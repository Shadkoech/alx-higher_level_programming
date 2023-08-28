#!/usr/bin/python3


def safe_print_division(a, b):
    """This is a function that divides two integers and returns result"""

    try:
        quotient = a / b

    except (ZeroDivisionError, TypeError):
        quotient = None

    finally:
        print("Inside result: {}".format(quotient))

    return (quotient)
