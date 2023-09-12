#!/usr/bin/python3
"""
A python module where a line is inserted into a file after
a line that contains a specific string"""


def append_after(filename="", search_string="", new_string=""):
    """
    append_after: A function that inserts a line of text after
    a given specific string
    Args:
        filename - name of the file to append
        search_String - the specific string to search for
        new_string - The line of text to insert
    """

    with open(filename, "r") as f:
        '''In this case, readlines fxn is used to scheme through
        the file and store the strings in a variable call it
        text'''

        text = f.readlines()

    with open(filename, "w") as f:
        '''Here we iterate over our text(lines of strings) and
        each time we get the specific string(search_string) we
        append with the new_string'''

        for line in text:
            f.write(line)
            if search_string in line:
                f.write(new_string)
