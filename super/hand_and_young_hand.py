
#! /usr/bin/env python

def do_small_eye(str_arg):
    large_place(str_arg)
    print('large_thing')

def large_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_small_eye('last_number')
