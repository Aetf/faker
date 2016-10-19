
#! /usr/bin/env python

def point_and_same_number(str_arg):
    public_child(str_arg)
    print('big_child')

def public_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point_and_same_number('fact')
