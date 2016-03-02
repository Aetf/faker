
#! /usr/bin/env python

def work(str_arg):
    long_hand(str_arg)
    print('thing')

def long_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('year')
