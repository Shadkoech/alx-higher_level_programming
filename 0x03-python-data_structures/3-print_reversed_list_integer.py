#!/usr/bin/python3

# list reversal
def print_reversed_list_integer(my_list=[]):
    '''Printing all list integers in reverse'''
    for i in range(len(my_list)-1, -1, -1):
        print("{:d}".format(my_list[i]))
