
#! /usr/bin/env python

def make_part(str_arg):
    tell_old_thing(str_arg)
    print('first_time')

def tell_old_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_part('week')
