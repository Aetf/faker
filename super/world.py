
#! /usr/bin/env python

def big_world(str_arg):
    child(str_arg)
    print('big_child_or_different_group')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_world('think_great_case')
