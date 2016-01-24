
#! /usr/bin/env python

def good_life(str_arg):
    man(str_arg)
    print('work')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_life('other_case')
