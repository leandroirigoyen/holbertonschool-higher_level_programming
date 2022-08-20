#!/bin/bash
# sends a JSON POST request to a url passed, displays the body
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
