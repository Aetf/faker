
#! /usr/bin/env python

def first_life(str_arg):
    next_way(str_arg)
    print('child')

def next_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_life('person')
