
#! /usr/bin/env python

def hand(str_arg):
    world_and_first_child(str_arg)
    print('number')

def world_and_first_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('hand')
