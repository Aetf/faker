
#! /usr/bin/env python

def other_child(str_arg):
    hand_or_place(str_arg)
    print('come_own_child')

def hand_or_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('woman')
