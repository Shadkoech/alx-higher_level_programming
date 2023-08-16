#!/usr/bin/python3

# checking presence of and deleting a key

def simple_delete(a_dictionary, key=""):
    """This is a function deleting a key in a dictionary"""

    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
