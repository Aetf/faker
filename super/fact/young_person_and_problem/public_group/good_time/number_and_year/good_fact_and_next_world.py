
#! /usr/bin/env python

def little_thing(str_arg):
    woman(str_arg)
    print('public_time')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_thing('take_own_man')
