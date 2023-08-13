#!/usr/bin/python3

# tuple from a sentence
def multiple_returns(sentence):
    """function returning a tuple with len of string and first char"""

    kl_tuple = ()
    if len(sentence) == 0:
        kl_tuple = (0, "None")
    else:
        kl_tuple = (len(sentence), sentence[0])
        return kl_tuple
