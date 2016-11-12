
#! /usr/bin/env python

def group(str_arg):
    long_life(str_arg)
    print('group')

def long_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('large_place')
