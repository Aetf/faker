
#! /usr/bin/env python

def own_year(str_arg):
    make_thing(str_arg)
    print('child')

def make_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_year('big_place')
