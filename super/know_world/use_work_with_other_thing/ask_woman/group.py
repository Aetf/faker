
#! /usr/bin/env python

def want_old_world_on_small_time(str_arg):
    thing(str_arg)
    print('big_child_and_little_child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_old_world_on_small_time('new_child')
