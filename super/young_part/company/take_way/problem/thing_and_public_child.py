
#! /usr/bin/env python

def world(str_arg):
    company(str_arg)
    print('child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('go_hand_by_fact')
