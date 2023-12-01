#!/usr/bin/python3
"""
Python script that fetches https://alx-intranet.hbtn.io/status
"""

from urllib import request

url = 'https://alx-intranet.hbtn.io/status'

with request.urlopen(url) as response:
    body = response.read()
