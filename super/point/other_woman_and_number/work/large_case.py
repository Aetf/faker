
#! /usr/bin/env python

def have_point(str_arg):
    small_man(str_arg)
    print('world')

def small_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_point('child')
