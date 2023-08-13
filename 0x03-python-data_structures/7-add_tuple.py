#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    '''Function that adds up two tuples'''
    # Ensuring that both tuples have atleast 2 elements
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # sums of 1st and 2nd elements
    sum_first_element = tuple_a[0] + tuple_b[0]
    sum_second_element = tuple_a[1] + tuple_b[1]

    summed_tuple = (sum_first_element, sum_second_element)
    return summed_tuple
