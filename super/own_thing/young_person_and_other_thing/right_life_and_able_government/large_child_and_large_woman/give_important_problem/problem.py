
#! /usr/bin/env python

def good_case(str_arg):
    same_world(str_arg)
    print('point')

def same_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_case('man')
