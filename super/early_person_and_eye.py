
#! /usr/bin/env python

def hand(str_arg):
    point(str_arg)
    print('new_child')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('ask_person')
