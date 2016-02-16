
#! /usr/bin/env python

def bad_point(str_arg):
    long_thing(str_arg)
    print('child_and_last_point')

def long_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_point('eye')
