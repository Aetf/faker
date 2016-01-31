
#! /usr/bin/env python

def old_thing_and_hand(str_arg):
    child(str_arg)
    print('world')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_thing_and_hand('find_last_fact')
