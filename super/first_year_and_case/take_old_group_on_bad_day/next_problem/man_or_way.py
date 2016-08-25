
#! /usr/bin/env python

def life(str_arg):
    hand_and_last_man(str_arg)
    print('call_new_thing_beneath_other_man')

def hand_and_last_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('group')
