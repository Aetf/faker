
#! /usr/bin/env python

def own_world(str_arg):
    world(str_arg)
    print('small_life_and_world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_world('number')
