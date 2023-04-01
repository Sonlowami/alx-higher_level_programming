#!/usr/bin/python3
"""Try fetch a resiurce and catch an HTTPError"""


def main():
    """fetch a resource or get error"""

    import requests
    import sys
    data = {"email": sys.argv[2]}
    resp = requests.post(sys.argv[1], data)
    print(resp.text)


if __name__ == '__main__':
    main()
