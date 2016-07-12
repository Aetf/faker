
#! /usr/bin/env python

def child(str_arg):
    first_hand_and_small_child(str_arg)
    print('hand')

def first_hand_and_small_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('public_problem')
