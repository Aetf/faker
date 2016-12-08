
#! /usr/bin/env python

def number(str_arg):
    have_child(str_arg)
    print('same_child')

def have_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number('right_place')
