
#! /usr/bin/env python

def hand(str_arg):
    say_small_thing(str_arg)
    print('have_hand_for_world')

def say_small_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('group')
