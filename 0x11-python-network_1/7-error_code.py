#!/usr/bin/python3
"""Check the status code"""


def main():
    """This function checks whether the server did not
       return an http error message"""
    import requests
    from sys import argv
    resp = requests.get(argv[1])
    if resp.ok:
        print(resp.text)
    else:
        print("Error code: {}", resp.status)
