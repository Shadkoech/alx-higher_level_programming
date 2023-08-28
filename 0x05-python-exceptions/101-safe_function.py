#!/usr/bin/python3

# stderr needs sys importation
import sys


def safe_function(fct, *args):
    '''function executing another function safely
    fct in this case is used as a function pointer'''

    try:
        funcresult = fct(*args)

    except Exception as e:
        print("Exception:", e, file=sys.stderr)
        funcresult = None

    return funcresult
