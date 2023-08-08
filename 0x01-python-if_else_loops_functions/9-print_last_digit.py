#!/usr/bin/python3

# Printing the last digit of a number
def print_last_digit(number):
    '''Applying modulo to extract the last number'''
    lastdigit = (abs(number) % 10)
    print(lastdigit, end="")
    return lastdigit
