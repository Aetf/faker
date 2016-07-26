
#! /usr/bin/env python

def child_or_own_place(str_arg):
    thing(str_arg)
    print('company')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_own_place('public_life_or_own_thing')
