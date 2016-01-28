
#! /usr/bin/env python

def child(str_arg):
    long_world(str_arg)
    print('fact')

def long_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('time_or_little_life')
