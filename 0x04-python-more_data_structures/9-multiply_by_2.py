#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    '''Function that returns a dictionary with values multiplied by 2'''
    new_diction = {}

    for k, v in a_dictionary.items():
        new_diction[k] = v * 2

    return new_diction
