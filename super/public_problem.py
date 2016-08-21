
#! /usr/bin/env python

def man(str_arg):
    make_hand(str_arg)
    print('hand_or_thing')

def make_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('week')
