
#! /usr/bin/env python

def long_woman(str_arg):
    long_work(str_arg)
    print('bad_place')

def long_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_woman('own_man_or_early_case')
