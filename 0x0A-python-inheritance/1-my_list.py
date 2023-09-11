#!/usr/bin/python3
"""
class Mylist that inherits out of parent list
All the element of inherited type must be int
"""


class MyList(list):
    """
    Child/derived class and the parent is list class
    """

    def print_sorted(self):
        """
        method that prints the list and in ascending
        order
        """
        sorted_list_ascending = sorted(self)
        print(sorted_list_ascending)
