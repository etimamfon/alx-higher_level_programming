#!/bin/python3

# a Python script that fetches https://alx-intranet.hbtn.io/status


"""fetches https://alx-intranet.hbtn.io/status"""

# import request from urllib

from urllib import request

if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
