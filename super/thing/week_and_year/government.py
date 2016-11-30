
#! /usr/bin/env python

def give_world(str_arg):
    world(str_arg)
    print('world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_world('world')
