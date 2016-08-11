
#! /usr/bin/env python

def try_case(str_arg):
    world_or_early_world(str_arg)
    print('world')

def world_or_early_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_case('big_day')
