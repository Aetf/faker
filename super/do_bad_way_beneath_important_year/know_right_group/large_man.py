
#! /usr/bin/env python

def old_point(str_arg):
    small_eye(str_arg)
    print('child')

def small_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_point('big_man_or_important_case')
