#!/usr/bin/python3
""" Python module that takes in a letter and sends
POST req to http://0.0.0.0:5000/search_user with
letter as parameter"""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    try:
        req = requests.get(url, data=data)
        req_json = req.json()

        if req_json:
            print(f"[{response_json['id']}] {response_json['name']}")
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
