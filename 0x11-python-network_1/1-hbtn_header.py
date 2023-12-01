#!/usr/bin/python3

"""Python script that takes in URL, sends a req to it
and displays the value of X-Request-Id"""

import sys
import urllib.request

if __name__ == "__main__":

    url = sys.argv[1]

    req_object = urllib.request.Request(url)
    with urllib.request.urlopen(req_object) as response:
        print(dict(response.headers).get("X-Request-Id"))
