
#! /usr/bin/env python

def man(str_arg):
    world_and_thing(str_arg)
    print('large_thing')

def world_and_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('life')
