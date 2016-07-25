
#! /usr/bin/env python

def long_thing(str_arg):
    new_point(str_arg)
    print('take_own_point_about_point')

def new_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_thing('man')
