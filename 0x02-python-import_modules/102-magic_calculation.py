#!/usr/bin/python3

def magic_calculation(a, b):
    '''Obtaining a match for the bytecode given'''

    from magic_calculation_102 import *

    if (a < b):
        C = add(a, b)

        for index in range(4, 6):
            C = add(C, index)
        return (C)

    else:
        return (sub(a, b))
