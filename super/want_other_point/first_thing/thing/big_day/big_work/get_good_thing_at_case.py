
#! /usr/bin/env python

def long_world(str_arg):
    say_life(str_arg)
    print('new_child')

def say_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_world('government')
