
#! /usr/bin/env python

def try_little_thing(str_arg):
    other_life(str_arg)
    print('new_life')

def other_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_little_thing('case')
