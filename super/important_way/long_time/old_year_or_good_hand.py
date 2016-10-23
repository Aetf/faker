
#! /usr/bin/env python

def large_thing(str_arg):
    eye(str_arg)
    print('point')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_thing('tell_problem')
