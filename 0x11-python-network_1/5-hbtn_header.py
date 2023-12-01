#!/usr/bin/python3

"""Python script that takes in URL, sends a req to it
and displays the value of X-Request-Id in response
header"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]

    req = requests.get(url)
    print(req.headers.get("X-Request-Id"))
