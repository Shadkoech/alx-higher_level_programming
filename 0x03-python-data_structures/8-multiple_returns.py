#!/usr/bin/python3

def multiple_returns(sentence):
    """function returning a tuple with len of string and first char"""

    x = len(sentence)
    y = sentence[0]

    if x == 0:
        y == None
    else:
        my_tuple = (x, y)
        return my_tuple
