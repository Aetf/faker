
#! /usr/bin/env python

def right_place(str_arg):
    man(str_arg)
    print('person')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_place('government')
