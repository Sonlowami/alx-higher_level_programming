#!/usr/bin/python3
"""Send POST data in a parameter named 'q'"""


def main():
    """Does not run when executed"""
    import requests
    import sys
    data = {}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    else:
        data['q'] = ''
    resp = requests.post('http://0.0.0.0:5000/search_user', data)
    try:
        r = resp.json()
        if len(r) == 0:
            print("no result")
            return
        print(r)
    except ValueError:
        print("Not a valid JSON")


if __name__ == '__main__':
    main()
