#!/usr/bin/python3

# Using two indexes to represent the numbers 8 and 9
for m in range(9):
    for n in range(True, 10):
        if m == 8 and n == 9:
            print('{}{}'.format(m, n))
        elif m < n:
            print('{}{}, '.format(m, n), end="")
