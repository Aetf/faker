
#! /usr/bin/env python

def next_number_or_child(str_arg):
    world(str_arg)
    print('child')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_number_or_child('new_government')
