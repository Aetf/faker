
#! /usr/bin/env python

def long_thing(str_arg):
    little_man(str_arg)
    print('bad_thing')

def little_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_thing('right_group')
