#!/bin/bash
#script taking in URL as argument; sends GET request to the URL, then displays the reponse body
curl -sH "X-School-User-Id: 98" "$1"
