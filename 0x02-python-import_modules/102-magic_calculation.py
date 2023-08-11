#!/usr/bin/python3

# bytecode takes two arguments a and b and performs + or - to it
def magic_calculation(a, b):
    '''Obtaining a match for the bytecode given'''

    from magic_calculation_102 import add, sub

    if (a < b):
        c = add(a, b)

        for index in range(4, 6):
            c = add(c, index)
        return (c)

    else:
        return (sub(a, b))
