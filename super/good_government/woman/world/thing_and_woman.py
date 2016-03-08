
#! /usr/bin/env python

def hand(str_arg):
    thing(str_arg)
    print('last_thing')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('day')
