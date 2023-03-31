#!/usr/bin/python3

"""Take in a URL, send request to URL and display value of `X-Request-Id` variable found in the header of the response"""

import sys

from urllib import request

if __name__ == "__main__":
    with request.urlopen(sys.argv[1]) as res:
        print(res.info()['X-Request-Id'])
