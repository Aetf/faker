
#! /usr/bin/env python

def big_thing(str_arg):
    other_hand(str_arg)
    print('bad_place')

def other_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_thing('person')
