#!/usr/bin/env python

import sys
from trace_call_args import trace_call_args


def add(x, y):
    return x + y

def add_with_defaults(x=49, y=50):
    return x + y

if __name__ == '__main__':
    sys.settrace(trace_call_args)
    add(1, 2)
    add_with_defaults()
    sys.settrace(None)
