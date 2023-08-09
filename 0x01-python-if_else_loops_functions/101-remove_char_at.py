#!/usr/bin/python3

# Function that creates a copy of the string
# Removes a character at a position n (C array index)

def remove_char_at(str, n):
    if (n < 0 or n >= len(str)):
        return (str)
    else:
        newcopied_str = str[:n] + str[n + 1:]
    return newcopied_str
