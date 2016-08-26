
#! /usr/bin/env python

def time(str_arg):
    do_hand(str_arg)
    print('child')

def do_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('company')
