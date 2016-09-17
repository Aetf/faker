
#! /usr/bin/env python

def hand(str_arg):
    call_bad_case(str_arg)
    print('man')

def call_bad_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('new_world')
