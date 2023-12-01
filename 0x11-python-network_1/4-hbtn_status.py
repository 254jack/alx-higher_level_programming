#!/usr/bin/python3
"""Script that fetches url https://alx-intranet.hbtn.io/status."""
import requests


if __name__ == "__main__":
    url = requests.get("https://alx-intranet.hbtn.io/status")
