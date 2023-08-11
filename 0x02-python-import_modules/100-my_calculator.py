#!/usr/bin/python3

if __name__ == "__main__":
    '''importing all fxns and performing arithmetic operations'''

    import sys
    from calculator_1 import add, sub, mul, div

    no_arg = len(sys.argv)

    if no_arg != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    arith_operator = sys.argv[2]
    if arith_operator not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    # getting the integer values from the argument
    a = int(sys.argv[1])
    b = int(sys.argv[3])

    # into arithmetic operations
    if arith_operator == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif arith_operator == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif arith_operator == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, div(a, b)))
