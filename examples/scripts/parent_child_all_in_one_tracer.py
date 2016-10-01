#!/usr/bin/env python

import sys
from all_in_one import all_in_one_tracer

def child():
    for i in range(3):
        print(' ' * 8, 'in child loop')

def parent():
    for i in range(2):
        print(' ' * 4, 'in parent loop')
        child()

if __name__ == '__main__':
    sys.settrace(all_in_one_tracer)
    parent()
    sys.settrace(None)
