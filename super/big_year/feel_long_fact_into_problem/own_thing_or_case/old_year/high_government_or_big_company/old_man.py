
#! /usr/bin/env python

def world(str_arg):
    small_thing(str_arg)
    print('other_work_or_thing')

def small_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('right_week')
