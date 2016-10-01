#!/usr/bin/env python

import sys
from trace_call_args import trace_call_args_2


def var_args(*args, **kwargs):
    x = 1
    y = 2
    return x, y

if __name__ == '__main__':
    sys.settrace(trace_call_args_2)

    args = (1, 2, 'foo')
    kwargs = {'a': 8, 'b': 9}
    var_args(*args, **kwargs)

    sys.settrace(None)
