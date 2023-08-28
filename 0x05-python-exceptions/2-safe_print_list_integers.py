#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """Funtion that prints only integer values of a list"""

    num = 0
    for element in range(x):
        try:
            print("{:d}".format(my_list[element]), end="")
            num += 1

        except (ValueError, TypeError):
            pass

    print()
    return num
