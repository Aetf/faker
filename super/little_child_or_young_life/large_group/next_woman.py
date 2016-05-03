
#! /usr/bin/env python

def next_part(str_arg):
    bad_part(str_arg)
    print('child')

def bad_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_part('say_work')
