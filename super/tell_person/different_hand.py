
#! /usr/bin/env python

def first_eye(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_eye('young_child')
