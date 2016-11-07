
#! /usr/bin/env python

def make_world(str_arg):
    point_and_high_world(str_arg)
    print('right_hand')

def point_and_high_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_world('other_person')
