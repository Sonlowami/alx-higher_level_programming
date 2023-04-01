#!/usr/bin/python3
"""Send a post request"""


def main():
    """send a post request"""

    from urllib import request, parse
    from sys import argv
    recipient = {'email': argv[2]}
    data = parse.urlencode(recipient).encode("utf-8")
    req = request.Request(argv[1], data)
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))


if __name__ == '__main__':
    main()
