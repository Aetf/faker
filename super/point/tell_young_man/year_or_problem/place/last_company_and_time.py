
#! /usr/bin/env python

def do_large_life(str_arg):
    little_fact(str_arg)
    print('child')

def little_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_large_life('case')
