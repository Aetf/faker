
#! /usr/bin/env python

def other_eye(str_arg):
    point(str_arg)
    print('public_point')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_eye('public_hand_and_early_fact')
