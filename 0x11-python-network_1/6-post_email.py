#!/usr/bin/python3
""" Python module that takes in URL and an email then
sends a POST request to the passed URL with email as
parameter"""

import sys
import requests

if __name__ == "__main__":

    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    req = requests.post(url, value)
    print(req.text)
