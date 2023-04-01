#!/usr/bin/python3
"""find value of a header 'X-Request-Id' using requests"""


def main():
    """find value of a header"""
    import requests
    from sys import argv
    data = requests.get(argv[1])
    try:
        print(data.headers['X-Request-Id'])
    except KeyError:
        pass


if __name__ == '__main__':
    main()
