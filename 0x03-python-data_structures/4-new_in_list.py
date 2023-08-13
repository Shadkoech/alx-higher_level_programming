#!/usr/bin/python3

# say index 2: [1, 2, 3, 4] => [1, 2, 9, 4]

def new_in_list(my_list, idx, element):
    '''replace an element at a given index'''
    copied_list = my_list.copy()
    if idx < 0:
        return copied_list
    elif idx > len(my_list) - 1:
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list
