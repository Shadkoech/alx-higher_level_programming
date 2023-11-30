#!/bin/bash
#Script sending DELETE request to URL passed as first argument theb displays response body
curl -s "$1" -X DELETE
