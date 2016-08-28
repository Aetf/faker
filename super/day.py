
#! /usr/bin/env python

def work(str_arg):
    child(str_arg)
    print('thing')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('world')
