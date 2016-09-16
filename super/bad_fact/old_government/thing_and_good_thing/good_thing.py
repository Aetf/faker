
#! /usr/bin/env python

def child(str_arg):
    bad_life(str_arg)
    print('next_world')

def bad_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('case')
