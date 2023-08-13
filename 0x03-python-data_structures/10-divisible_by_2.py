#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    '''Function that captures multiples of two in a list'''

    mynew_list = []

    for i in my_list:
        if i % 2 == 0:
            mynew_list.append(True)
        else:
            mynew_list.append(False)

    return mynew_list
