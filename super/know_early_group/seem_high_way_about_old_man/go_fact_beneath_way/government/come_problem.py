
#! /usr/bin/env python

def company(str_arg):
    first_group(str_arg)
    print('child')

def first_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('life')
