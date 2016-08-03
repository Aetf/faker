
#! /usr/bin/env python

def do_early_hand(str_arg):
    world(str_arg)
    print('thing')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_early_hand('company')
