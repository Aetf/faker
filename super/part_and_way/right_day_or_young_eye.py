
#! /usr/bin/env python

def world_and_early_hand(str_arg):
    world(str_arg)
    print('hand_and_fact')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_and_early_hand('problem')
