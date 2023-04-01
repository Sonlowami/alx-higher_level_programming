#!/usr/bin/python3
"""This module contains a function that fetches from the intranet"""


def main():
    """fetch the intranet"""

    from urllib import request
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        resp = resp.read()
        print("Body response:\n\t- type: {}\n\t- content: {}"
             .format(type(resp), resp))
        print("\t- utf8 content: {}".format(resp.decode('utf-8')))


if __name__ == '__main__':
    main()
