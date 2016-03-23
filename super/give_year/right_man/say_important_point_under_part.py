
#! /usr/bin/env python

def place_and_early_place(str_arg):
    call_long_time(str_arg)
    print('case')

def call_long_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place_and_early_place('world')
