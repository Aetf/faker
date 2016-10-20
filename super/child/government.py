
#! /usr/bin/env python

def world(str_arg):
    first_group(str_arg)
    print('small_group')

def first_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('group')
