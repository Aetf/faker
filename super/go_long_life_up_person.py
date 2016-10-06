
#! /usr/bin/env python

def long_work(str_arg):
    want_important_hand(str_arg)
    print('early_way')

def want_important_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('child')
