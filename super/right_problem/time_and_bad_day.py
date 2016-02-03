
#! /usr/bin/env python

def good_world_and_hand(str_arg):
    little_thing(str_arg)
    print('child')

def little_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_world_and_hand('week')
