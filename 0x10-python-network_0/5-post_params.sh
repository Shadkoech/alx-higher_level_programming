#!/bin/bash
#script taking  in a URL, sends a POST request to the passed URL;displays response body
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
