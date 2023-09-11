#!/usr/bin/python3
"""
A module that creates a new class MyInt that inherits
From int
MyInt class is a rebel and has == and != inverted
"""


class MyInt(int):
    """ A rebel class with == and != inverted
    """

    def __eq__(self, value):
        """This function flips the == operator and replaces
        it with !="""
        return self.real != value

    def __ne__(self, value):
        """Flips the != operator and replaces it with
        == """
        return self.real == value
