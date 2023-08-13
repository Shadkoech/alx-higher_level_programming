#!/usr/bin/python3

# printing all values(integers) of list called my_list
def print_list_integer(my_list=[]):
    '''Printing all integers of a list'''
    for index in range(len(my_list)):
        print("{}".format(my_list[index]))
