#!/usr/bin/python3

# going through the diction for the biggest value

def best_score(a_dictionary):
    """Function returning a key with the biggest integer"""

    if not a_dictionary:
        return None
    else:
        return max(a_dictionary, key=a_dictionary.get, default=None)
