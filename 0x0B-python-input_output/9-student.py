#!/usr/bin/python3
"""
A python module that instantiates a class
"""


class Student:
    """
    class that defines a student
    """

    def __init__(self, first_name, last_name, age):
        """attribute instance constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ class public method that retrieves dictionary
        representation of a Student"""
        return self.__dict__
