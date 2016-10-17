
#! /usr/bin/env python

def long_work(str_arg):
    old_case(str_arg)
    print('long_case')

def old_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work('high_day')
