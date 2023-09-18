#!/usr/bin/python3
"""
This is a base for all the classes herein
"""
import json
import csv


class Base:
    """Base class for all ensuing classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization of the class Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Method that returns JSON string representation of list of
        dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """class method that writes JSON string representation of
        list_objs to a file"""

        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")

            else:
                list_dictionaries = [o.to_dictionary() for o in list_objs]
                json_file.write(Base.to_json_string(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Method that returns list of JSON string
        representation json_string"""

        if json_string is None or json_string == []:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """class method that returns an instance with all the set
        attributes that will be used for the deserialization of a
        csv file"""
        if cls.__name__ == "Rectangle":
            new_instance = cls(4, 6)
        if cls.__name__ == "Square":
            new_instance = cls(4)

        new_instance.update(**dictionary)
        return new_instance

    @classmethod
    def load_from_file(cls):
        """class method that returns a list of instances"""
        filename = cls.__name__ + ".json"
        instance_list = []
        try:
            with open(filename, "r") as f:
                json_string = f.read()
                dictionary_list= cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list






