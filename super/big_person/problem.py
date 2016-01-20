
#! /usr/bin/env python

def hand(str_arg):
    company(str_arg)
    print('child')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('same_week')
