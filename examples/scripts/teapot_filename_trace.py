#!/usr/bin/env python

import sys

import requests

from filename_trace import filename_tracer


def teapot():
    url = 'http://httpbin.org/status/418'
    resp = requests.get(url)
    print(resp.status_code, resp.reason)
    print(resp.text)

if __name__ == '__main__':
    sys.settrace(filename_tracer)
    teapot()
    sys.settrace(None)
