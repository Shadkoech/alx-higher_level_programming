#!/usr/bin/python3

def fizzbuzz():
    """For multiples of 3 print fizz, multiples of 5 buzz
    multiples of 5 and 3 fizzbuzz"""
    for num in range(1, 101):
        if (num % 15) == 0:
            print("FizzBuzz ", end="")
        elif (num % 3) == 0:
            print("Fizz ", end="")
        elif (num % 5) == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(num), end="")
