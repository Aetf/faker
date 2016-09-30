
#! /usr/bin/env python

def thing(str_arg):
    first_group(str_arg)
    print('right_place_and_time')

def first_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('take_group')
