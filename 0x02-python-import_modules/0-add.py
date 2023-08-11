#!/usr/bin/python3

# Imports the def add(a,b) function from add_0.py
if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    output = add(a, b)

    print(f"{a} + {b} = {output}")
