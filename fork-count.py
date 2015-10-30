#!/usr/bin/env python3

'''
    In this program I'm trying to use parallel programming, using examples
    in Mark Lutz Learning Python.
    Запускает 5 копий себя самого, при этом каждая копия считает 5 с
    односекундной задержкой.
'''

import os, time

def counter(count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), i))

if __name__== '__main__':
    for i in range(5):
        pid = os.fork()
        if pid != 0:
            print('Process %d spawned' % pid)
        else:
            counter(5)
            os._exit(0)
    print('Main process exiting')
