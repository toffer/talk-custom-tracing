#!/usr/bin/env python

import requests


def teapot():
    url = 'http://httpbin.org/status/418'
    resp = requests.get(url)
    print(resp.status_code, resp.reason)
    print(resp.text)

teapot()
