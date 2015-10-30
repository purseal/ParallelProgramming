#!/usr/bin/env python3

'''
    In this program I'm trying to use parallel programming, using examples
    in Mark Lutz Learning Python.
    Ответвляет дочерние процессы, пока не будет нажата клавиша q.
'''

import os

def child():
    print('Hello from child', os.getpid())
    os._exit(0)

def parent():
    while True:
        newpid = os.fork()
        if newpid == 0:
            child()
        else:
            print('Hello from parent', os.getpid(), newpid)
        if input() == 'q':
            break

if __name__ == "__main__":
    parent()
