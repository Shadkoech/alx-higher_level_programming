#!/usr/bin/python3
"""
A Python script that adds all available arguments to a python list
then saves them all to a given file
"""
import sys

if __name__ == "__main__":
    """function that specifies what block of code ought
    to be run on direct execution and not when imported
    """

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    try:
        addeditems = load_from_json_file("add_item.json")
    except FileNotFoundError:
        addeditems = []

        addeditems.extend(sys.argv[1:])
        save_to_json_file(addeditems, "add_item.json")
