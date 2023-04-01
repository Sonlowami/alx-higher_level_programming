#!/usr/bin/python3
"""Try and catch an HTTPError"""


def main():
    """fetch a resource or get error"""

    from urllib import request
    from urllib.error import HTTPError
    from sys import argv
    try:
        with request.urlopen("{}".format(argv[1])) as resp:
            resp = resp.read()
            print(resp.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))


if __name__ == '__main__':
    main()
