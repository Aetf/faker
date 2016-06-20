
#! /usr/bin/env python

def call_man(str_arg):
    last_world_or_small_man(str_arg)
    print('world')

def last_world_or_small_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_man('man')
