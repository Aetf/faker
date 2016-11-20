
#! /usr/bin/env python

def large_work(str_arg):
    first_hand(str_arg)
    print('long_life')

def first_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_work('group')
