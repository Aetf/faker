
#! /usr/bin/env python

def bad_way(str_arg):
    problem(str_arg)
    print('high_day')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_way('thing_or_long_way')
