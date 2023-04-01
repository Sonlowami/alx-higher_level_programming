#!/usr/bin/python3
"""fetch from theintranet using requests"""


def main():
    """fetch a resource"""
    import requests
    data = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(data.text), data.text))


if __name__ == '__main__':
    main()
