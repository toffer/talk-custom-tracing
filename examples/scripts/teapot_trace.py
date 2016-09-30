#!/usr/bin/env python

import requests
from trace import Trace


def teapot():
    url = 'http://httpbin.org/status/418'
    resp = requests.get(url)
    print(resp.status_code, resp.reason)
    print(resp.text)

Trace().runfunc(teapot)
