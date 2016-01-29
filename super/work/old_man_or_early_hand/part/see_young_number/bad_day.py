
#! /usr/bin/env python

def large_hand(str_arg):
    good_company(str_arg)
    print('child')

def good_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_hand('last_government')
