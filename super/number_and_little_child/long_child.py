
#! /usr/bin/env python

def child(str_arg):
    group(str_arg)
    print('call_child')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('government')
