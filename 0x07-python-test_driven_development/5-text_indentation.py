#!/usr/bin/python3
"""
text_identation: A function printing text with 2 new lines on hitting .,?:
Args:
    text - The text to be printed
Raises:
    TypeError: text must be a string
"""


def text_indentation(text):
    """
    A function that prints a text on new line upon encountering .,? or :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    index = 0  # index initialized to zero which is used to iteract thru text

    while index < len(text) and text[index] == " ":
        index += 1

    while index < len(text):  # main loop iterating thru entire txt
        print(text[index], end="")
        if text[index] == "\n" or text[index] in ".?:":
            if text[index] in ".?:":
                print("\n")

            index += 1
            while index < len(text) and text[index] == " ":
                index += 1
            continue
        index += 1
