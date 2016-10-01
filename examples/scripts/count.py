#!/usr/bin/env python

import sys
from multiple_tracers import (system_tracer,
        local_tracer)

def count_one():
    print('1')
    return 'Done'

def count_two():
    print('one')
    print('two')
    return 'Done'

if __name__ == '__main__':
    sys.settrace(system_tracer)
    count_one()
    count_two()
    sys.settrace(None)
