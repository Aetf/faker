
#! /usr/bin/env python

def small_child(str_arg):
    new_case(str_arg)
    print('life')

def new_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_child('go_way_after_own_case')
