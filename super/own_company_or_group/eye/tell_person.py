
#! /usr/bin/env python

def small_eye(str_arg):
    child(str_arg)
    print('child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_eye('great_year')
