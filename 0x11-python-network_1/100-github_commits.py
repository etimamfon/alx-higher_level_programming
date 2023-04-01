#!/usr/bin/python3
"""
lists 10 commits (from the most recent to oldest)
of the provided repository and owner
"""
from sys import argv
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    r = requests.get(url)
    d = r.json()
    for _ in d[0:10]:
        print(_.get('sha'), end=': ')
        print(_.get('commit').get('author').get('name'))
