
#! /usr/bin/env python

def bad_time(str_arg):
    fact(str_arg)
    print('world')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_time('own_time')
