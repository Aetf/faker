
#! /usr/bin/env python

def take_other_way(str_arg):
    world(str_arg)
    print('little_life')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_other_way('thing')
