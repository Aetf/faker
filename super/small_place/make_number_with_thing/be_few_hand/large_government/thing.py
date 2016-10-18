
#! /usr/bin/env python

def large_thing(str_arg):
    call_fact(str_arg)
    print('look_large_time')

def call_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_thing('time')
