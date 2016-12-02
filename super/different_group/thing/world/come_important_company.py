
#! /usr/bin/env python

def hand(str_arg):
    group(str_arg)
    print('child_or_first_case')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('long_government')
