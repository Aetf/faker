
#! /usr/bin/env python

def company(str_arg):
    old_case(str_arg)
    print('child')

def old_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('new_man')
