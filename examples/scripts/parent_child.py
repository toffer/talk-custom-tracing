#!/usr/bin/env python

def child():
    for i in range(3):
        print(' ' * 8, 'in child loop')

def parent():
    for i in range(2):
        print(' ' * 4, 'in parent loop')
        child()

if __name__ == '__main__':
    print('main start')
    parent()
    print('main end')
