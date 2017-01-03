
#! /usr/bin/env python

def child(str_arg):
    man_or_big_hand(str_arg)
    print('next_group')

def man_or_big_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('large_fact')
