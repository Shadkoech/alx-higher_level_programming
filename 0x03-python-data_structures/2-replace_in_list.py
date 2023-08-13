#!/usr/bin/python3

# Replacing an element at an index
def replace_in_list(my_list, idx, element):
    '''replacement in a list'''

    if idx < 0:
        return my_list
    elif idx > (len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
