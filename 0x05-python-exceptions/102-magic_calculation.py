#!/usr/bin/python3


def magic_calculation(a, b):
    """ bytcode function doing magic calculation
    it return a / b ** i"""

    resul = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                resul += (a ** b) / i

        except Exception:
            resul = a + b

        return (resul)
