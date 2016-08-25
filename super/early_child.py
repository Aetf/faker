
#! /usr/bin/env python

def own_world(str_arg):
    number(str_arg)
    print('public_time')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_world('thing')
