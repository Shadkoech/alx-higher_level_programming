#!/usr/bin/python3


def update_dictionary(a_dictionary, key, value):
    '''function replacing or adding key/value in a dictionary
    key data type must always be string
    the value could be
    any(string,int,tuple,set or other dict)'''

    a_dictionary[key] = value
    return a_dictionary
