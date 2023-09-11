#!/usr/bin/python3
"""
A module that creates a new class MyInt that inherits From int
"""


class MyInt(int):
    """ A rebel class with == and != inverted
    """

    def __eq__(self, other):
        """This function flips the == operator and replaces
        it with !="""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Flips the != operator and replaces it with
        == """
        return super().__eq__(other)
