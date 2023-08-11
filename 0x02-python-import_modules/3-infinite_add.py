#!/usr/bin/python3

if __name__ == "__main__":
    """Adding all the arguments passed"""

    import sys
    no_arg = len(sys.argv)
    total_arg = 0

    for i in range(1, no_arg):
        total_arg += int(sys.argv[i])

    print(total_arg)
