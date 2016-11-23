
#! /usr/bin/env python

def own_thing(str_arg):
    man(str_arg)
    print('big_thing_and_bad_thing')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_thing('have_thing')
