#!/usr/bin/python3

""" Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""

import sys
import requests

if __name__ == "__main__":

    url = 'https://api.github.com/user'
    user = sys.argv[1]
    password = sys.argv[2]
    req = requests.get(url, auth=(user, password))

    try:
        json_req = req.json()
        print(json_req["id"])
    except Exception:
        print("None")
