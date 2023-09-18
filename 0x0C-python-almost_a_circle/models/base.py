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
                dictionary_list = cls.from_json_string(json_string)
                for item in dictionary_list:
                    instance = cls.create(**item)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass

        return instance_list

    # Advanced tasks
    # serialization and deserialization in CSV

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Method that performs serialization on list_objs in CSV format
        then saves it to a file"""

        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if list_objs is not None:
                list_objs = [i.to_dictionary() for i in list_objs]

                if cls.__name__ == "Rectangle":
                    fields = ["id", "width", "height", "x", "y"]
                if cls.__name__ == "Square":
                    fields = ["id", "size", "x", "y"]

                writer = csv.DictWriter(f, fieldnames=fields)
                writer.writeheader()
                writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        """Method that deserializes list of instances in CSV both
        filed and file names"""

        filename = cls.__name__ + ".csv"
        instance_list = []
        try:
            with open(filename, "r") as f:
                result = csv.DictReader(f)
                for row in result:
                    row = dict(row)
                    for key in row:
                        row[key] = int(row[key])
                    instance = cls.create(**row)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
