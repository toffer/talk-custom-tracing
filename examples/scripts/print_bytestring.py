#!/usr/bin/env python

import sys

def tracer(frame, event, arg):
    if event == 'call':
        print(frame.f_code.co_name)
        print(frame.f_code.co_code)
    return None

def parent():
    for i in range(3):
        child()
    return 'parent done'

def child():
    for i in range(5):
        print('in child loop')
    return 'child done'

if __name__ == '__main__':
    sys.settrace(tracer)
    parent()
    sys.settrace(None)
