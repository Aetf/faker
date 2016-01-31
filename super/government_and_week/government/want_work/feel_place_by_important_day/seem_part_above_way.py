
#! /usr/bin/env python

def hand(str_arg):
    want_same_thing(str_arg)
    print('long_part')

def want_same_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('last_number')
