#!/usr/bin/python3

# list reversal
def print_reversed_list_integer(my_list=[]):
    '''Printing all list integers in reverse'''
    if my_list is None:
        my_list = []

    for i in reversed(my_list):
        print("{:d}".format(i))
