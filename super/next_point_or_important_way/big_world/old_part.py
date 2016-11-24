
#! /usr/bin/env python

def man(str_arg):
    small_man(str_arg)
    print('company')

def small_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('large_thing_and_point')
