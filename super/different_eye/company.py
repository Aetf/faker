
#! /usr/bin/env python

def big_child(str_arg):
    different_number(str_arg)
    print('public_world_and_big_hand')

def different_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('place_and_company')
