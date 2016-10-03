
#! /usr/bin/env python

def world(str_arg):
    government(str_arg)
    print('old_world')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('first_child_or_point')
