
#! /usr/bin/env python

def call_thing_above_hand(str_arg):
    company(str_arg)
    print('company')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_thing_above_hand('big_number')
