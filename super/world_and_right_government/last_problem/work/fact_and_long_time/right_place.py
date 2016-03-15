
#! /usr/bin/env python

def time_or_world(str_arg):
    see_world(str_arg)
    print('work')

def see_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_or_world('thing_or_different_case')
