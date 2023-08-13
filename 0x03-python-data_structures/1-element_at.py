#!/usr/bin/python3

# getting element at an index within a list range
def element_at(my_list, idx):
    '''Retrieving an element from a list'''
    if idx < 1:
        return None
    elif idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
