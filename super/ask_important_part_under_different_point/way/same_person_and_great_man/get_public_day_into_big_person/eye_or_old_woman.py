
#! /usr/bin/env python

def say_thing_for_man(str_arg):
    do_world(str_arg)
    print('have_day')

def do_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_thing_for_man('different_group')
