#!/usr/bin/python3

def multiple_returns(sentence):
    """function returning a tuple with len of string and first char"""

    x = len(sentence)
    y = sentence[0]

    my_tuple = (x, y)

    if x == 0:
        return (None, None)
    else:
        return my_tuple
