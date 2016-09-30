#!/usr/bin/env python

def child():
    # Uh oh! ZeroDivisionError!
    return 1 / 0

def parent():
    return child()

if __name__ == '__main__':
    parent()
