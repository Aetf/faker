
#! /usr/bin/env python

def point(str_arg):
    child(str_arg)
    print('case')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('man')
