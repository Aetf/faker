
#! /usr/bin/env python

def hand(str_arg):
    say_thing(str_arg)
    print('right_part')

def say_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('week')
