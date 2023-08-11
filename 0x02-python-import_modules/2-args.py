#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    no_arg = len(sys.argv)  # gets all arguments + argv[0]

    if no_arg == 1:  # meaning 0 since we don't want arg[0]
        print("0 arguments.")
    elif no_arg == 2:  # i.e no_args == 1
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(no_arg - 1))

        for index in range(1, no_arg):
            print("{}: {}".format(index, sys.argv[index]))
