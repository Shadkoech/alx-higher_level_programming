#!/bin/bash
# A bash script taking in a URL, sends req. to it and display size of the response's body
curl -s "$1" | wc -c 
