# parent_child_trace.py

import sys
import time

from tracer_2 import ZipkinTracer

def child():
    for i in range(5):
        print('in child loop')
    return 'child done'

def parent():
    for i in range(3):
        child()
    return 'parent done'

def main():
    return parent()

if __name__ == '__main__':
    sys.settrace(ZipkinTracer())
    main()
    sys.settrace(None)
