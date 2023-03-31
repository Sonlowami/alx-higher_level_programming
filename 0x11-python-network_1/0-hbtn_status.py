#!/usr/bin/python3
"""fetch the intranet"""

def main():
    """fetch the intranet"""

    import urllib.request
    resp = urllib.request.urlopen("https://alx-intranet.hbtn.io/status").read()
    print("Body response:\n\t- type: {}\n\t- content: {}\n\t- utf8 content: {}"
          .format(type(resp), resp, resp.decode("utf-8")))


if __name__ == '__main__':
    main()
