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

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student
        instance"""
        if attrs is None:
            return self.__dict__

        elif all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__
