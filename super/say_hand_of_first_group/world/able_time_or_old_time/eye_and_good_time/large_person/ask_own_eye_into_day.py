
#! /usr/bin/env python

def own_part(str_arg):
    large_hand(str_arg)
    print('other_hand')

def large_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_part('public_world')
