#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    Lastdigit = -(number % 10)
else:
    Lastdigit = (number % 10)
if Lastdigit > 5:  # Assign message(Msg) in regard to last digit
    Msg = "and is greater than 5"
elif Lastdigit == 0:
    Msg = "and is 0"
else:
    Msg = "and is less than 6 and not 0"
print(F"Last digit of {number} is {Lastdigit} {Msg}")
