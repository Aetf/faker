
#! /usr/bin/env python

def do_hand(str_arg):
    point_or_last_world(str_arg)
    print('world')

def point_or_last_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_hand('man_and_thing')
