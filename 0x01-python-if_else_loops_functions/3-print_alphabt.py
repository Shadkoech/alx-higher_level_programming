#!/usr/bin/python3

# Print letters except q and e
for Letter in range(97, 123):
    if (Letter != 101 and Letter != 113):
        print("{}".format(chr(Letter)), end='')
