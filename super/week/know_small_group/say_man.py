
#! /usr/bin/env python

def say_hand(str_arg):
    world(str_arg)
    print('thing')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_hand('right_number')
