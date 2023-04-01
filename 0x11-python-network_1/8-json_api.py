#!/usr/bin/python3
"""Send POST data in a parameter named 'q'"""


def main():
    """Does not run when executed"""
    import requests
    import sys
    data = {}
    if len(sys.argv) > 0:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ''
    resp = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        if len(resp.json()) == 0:
            print("no result")
            return
        print(resp.json())
    except ValueError:
        print("Not a valid JSON")
