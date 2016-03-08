
#! /usr/bin/env python

def make_place(str_arg):
    have_place(str_arg)
    print('child')

def have_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_place('week')
