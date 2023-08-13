#!/usr/bin/python3


def max_integer(my_list=[]):
    '''Extracting biggest integer of a list'''

    if len(my_list) == 0:
        return None
    else:
        maxi_value = my_list[0]
        for i in range(len(my_list)):
            if my_list[i] > maxi_value:
                maxi_value = my_list[i]
        return maxi_value
