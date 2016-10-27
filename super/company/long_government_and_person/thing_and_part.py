
#! /usr/bin/env python

def life(str_arg):
    other_point(str_arg)
    print('public_child')

def other_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('same_eye')
