#!/usr/bin/python3
"""takes in a url, sends request, display the value of x-request-id"""
import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as url:
        s = url.getheader('X-Request-Id')
        print("{}".format(s))
