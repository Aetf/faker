
#! /usr/bin/env python

def bad_thing(str_arg):
    way(str_arg)
    print('public_day')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_thing('use_problem')
