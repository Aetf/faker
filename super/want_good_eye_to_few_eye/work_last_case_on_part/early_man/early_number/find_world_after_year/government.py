
#! /usr/bin/env python

def say_thing(str_arg):
    bad_man(str_arg)
    print('fact')

def bad_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_thing('try_different_thing_above_good_point')
