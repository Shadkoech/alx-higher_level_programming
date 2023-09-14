#!/usr/bin/python3

"""Module adding all arguments to python list then saves them to a file """

import sys


if __name__ == "__main__":

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = \
        __import__("6-load_from_json_file").load_from_json_file

    try:
        added_items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        added_items = []

        added_items.extend(sys.argv[1:])
        save_to_json_file(added_items, "add_item.json")
