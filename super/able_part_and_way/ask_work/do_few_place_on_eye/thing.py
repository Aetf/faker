
#! /usr/bin/env python

def time_or_small_point(str_arg):
    time(str_arg)
    print('case')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_or_small_point('call_company')
