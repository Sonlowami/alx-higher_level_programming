#!/usr/bin/python3
"""Try and catch an HTTPError"""


def main():
    """fetch a resource or get error"""

    from urllib import request
    from urllib.error import HTTPError
    from sys import argv
    with request.urlopen("{}".format(argv[1])) as resp:
        try:
            print(resp.read().decode("utf-8"))
        except HTTPError:
            print("Error code: {}".format(resp.status))


if __name__ == '__main__':
    main()
