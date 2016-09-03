
#! /usr/bin/env python

def right_hand_and_child(str_arg):
    bad_child(str_arg)
    print('new_world')

def bad_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_hand_and_child('know_company')
