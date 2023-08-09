#!/usr/bin/python3

# Print ASCII alphabet in reverse order
# Alternate upper and lower case
# last letter 'z' is small followed by upper 'Y'

for index in range(122, 96, -1):
    if index % 2 == 0:
        alphabet = chr(index)
    else:
        alphabet = chr(index - 32)
    print("{}".format(alphabet), end='')
