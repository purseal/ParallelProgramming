#!/usr/bin/env python3

''' Запускает программы, пока не будет нажата клавиша q. '''

import os

def run():
    parm = 0
    while True:
        parm += 1
        pid = os.fork()
        if pid == 0:
            os.execlp('python', 'python', 'child.py', str(parm))
            assert False, 'error starting program'
        else:
            print('Child is ', pid)
            if input() == 'q':
                break

if __name__ == '__main__':
    run()
