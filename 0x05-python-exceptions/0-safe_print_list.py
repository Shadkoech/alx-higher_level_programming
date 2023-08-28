#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """Function that prints out x elements from a list
    and return the number of elements printed"""

    num = 0
    for element in range(x):
        try:
            print("{}".format(my_list[element]), end='')
            num += 1

        except IndexError:
            pass

    print()  # this actually prints new line after elements
    return num
