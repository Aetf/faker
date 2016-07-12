
#! /usr/bin/env python

def hand(str_arg):
    thing(str_arg)
    print('group')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('get_hand_with_early_part')
