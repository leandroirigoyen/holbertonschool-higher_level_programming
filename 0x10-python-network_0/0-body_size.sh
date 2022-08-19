#!/bin/bash
# takes in url, sends request, display size of the body
curl -s "$1" | wc -c
