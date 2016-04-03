
#! /usr/bin/env python

def point(str_arg):
    same_fact(str_arg)
    print('public_thing')

def same_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('small_case')
