
#! /usr/bin/env python

def small_child(str_arg):
    public_world_and_year(str_arg)
    print('do_place')

def public_world_and_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_child('public_world')
