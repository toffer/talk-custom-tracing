# parent_child.py

import time


def child():
    for i in range(5):
        time.sleep(0.1)
        print('in child loop')
    return 'child done'

def parent():
    for i in range(3):
        time.sleep(0.2)
        child()
    return 'parent done'

def main():
    time.sleep(0.3)
    return parent()

if __name__ == '__main__':
    main()
