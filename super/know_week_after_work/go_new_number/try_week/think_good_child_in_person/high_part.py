
#! /usr/bin/env python

def group_and_world(str_arg):
    do_point_from_world(str_arg)
    print('world_and_thing')

def do_point_from_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group_and_world('thing_and_work')
