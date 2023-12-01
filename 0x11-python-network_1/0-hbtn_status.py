#!/usr/bin/python3
"""
script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib.request import Request, urlopen


if __name__ == "__main__":
    url = Request("https://alx-intranet.hbtn.io/status")
    with urlopen(url) as response:
        body = response.read()
