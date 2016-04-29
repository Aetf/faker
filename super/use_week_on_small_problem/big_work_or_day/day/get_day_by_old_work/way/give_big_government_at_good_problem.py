
#! /usr/bin/env python

def child(str_arg):
    world_or_life(str_arg)
    print('way')

def world_or_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('thing')
