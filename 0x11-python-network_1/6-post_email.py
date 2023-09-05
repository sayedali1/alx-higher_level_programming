#!/usr/bin/python3
"""
given URL & email as params
"""
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    payload = {'email': argv[2]}
    r = requests.post(url, data=payload)
    print(r.text)
