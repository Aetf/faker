
#! /usr/bin/env python

def call_time(str_arg):
    point_or_first_thing(str_arg)
    print('eye')

def point_or_first_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_time('bad_number')
