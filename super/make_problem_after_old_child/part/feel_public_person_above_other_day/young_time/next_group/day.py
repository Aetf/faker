
#! /usr/bin/env python

def other_place(str_arg):
    world(str_arg)
    print('world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_place('come_way_with_life')
