#!/usr/bin/python3
""" Python module that takes in URL and an email then
sends a POST request to the passed URL """

import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")  # ensure the data is in bytes

    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
