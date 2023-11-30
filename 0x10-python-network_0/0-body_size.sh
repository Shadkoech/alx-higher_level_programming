#!/usr/bin/bash
# A bash script taking in a URL, sends req. to it and display size of 
# the response's body

curl -sI "$1" | grep "Content-Length:" | cut -d' ' -f2
