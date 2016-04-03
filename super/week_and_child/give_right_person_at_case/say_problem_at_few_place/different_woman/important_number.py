
#! /usr/bin/env python

def long_company(str_arg):
    eye(str_arg)
    print('child')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_company('day_or_hand')
