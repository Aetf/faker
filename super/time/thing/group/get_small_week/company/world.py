
#! /usr/bin/env python

def go_hand_with_man(str_arg):
    small_thing(str_arg)
    print('man')

def small_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_hand_with_man('week')
