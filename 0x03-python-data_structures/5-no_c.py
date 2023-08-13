#!/usr/bin/python3

# removing from a string
def no_c(my_string):
    '''function that removes c and C from a string'''
    plucked_string = ""
    for index in my_string:
        if index != 'c' and index != 'C':
            plucked_string += index

    return plucked_string
