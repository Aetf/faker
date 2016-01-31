
#! /usr/bin/env python

def call_way(str_arg):
    say_great_number(str_arg)
    print('world')

def say_great_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_way('give_world_to_case')
