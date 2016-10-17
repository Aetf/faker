
#! /usr/bin/env python

def little_child(str_arg):
    world_or_point(str_arg)
    print('public_child')

def world_or_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_child('take_world_for_good_case')
