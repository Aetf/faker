
#! /usr/bin/env python

def child(str_arg):
    new_hand(str_arg)
    print('look_life')

def new_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('other_eye')
