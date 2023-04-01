#!/usr/bin/python3
"""print response header 'X-Request-Id'. Should be different
everytime"""

def main():
    """print a particular response header"""

    from urllib import request
    from sys import argv
    with request.urlopen("{}".format(argv[1])) as resp:
        print(resp.getheader('X-Request-Id'))


if __name__ == '__main__':
    main()
