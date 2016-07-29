
#! /usr/bin/env python

def world(str_arg):
    next_thing_and_way(str_arg)
    print('child')

def next_thing_and_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('good_number')
