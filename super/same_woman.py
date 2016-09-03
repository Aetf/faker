
#! /usr/bin/env python

def same_place(str_arg):
    first_place(str_arg)
    print('different_thing_and_great_time')

def first_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_place('time')
