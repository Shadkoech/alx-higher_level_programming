#!/usr/bin/python3


def uniq_add(my_list=[]):
    ''' Adds all the unique integers in a list'''

    uniq_int = set(my_list)

    total_uniq_int = sum(uniq_int)

    return total_uniq_int
