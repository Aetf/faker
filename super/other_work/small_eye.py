
#! /usr/bin/env python

def good_thing(str_arg):
    long_thing(str_arg)
    print('year')

def long_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_thing('next_life')
